from flask import Flask, render_template, request, redirect, url_for, flash, session
#from flask_login import LoginManager, login_user, logout_user, login_required
from config import config
import sqlite3
import os
from fastrading.fastrading import get_binance_symbols, fast_trade

app = Flask(__name__)
#login_manager_app = LoginManager(app)



@app.route('/fast_trade/action', methods=['GET','POST'])
def fast_trade_action():
    if session.get('logged_in'):
        # User is authenticated
        if request.method == 'POST':
            print("FAST_TRADE_VALUES: ",request.form)
            return render_template('fast_trade/trade_action.html',request=str(request.form))
        else:
            flash("Error on trade !")
            return redirect(url_for('fast_trade_home'))
    else:
        # Not logged user
        flash("You are not logged, try again cowboy")
        return redirect(url_for('login'))


@app.route('/fast_trade')
def fast_trade_home():
    if session.get('logged_in'):
        # User is authenticated
        print(get_binance_symbols())
        symbols = get_binance_symbols()
        return render_template('auth/main.html', username=session.get('username'), symbols=symbols)
    else:
        # Not logged user
        return redirect(url_for('login'))


@app.route('/', methods=['GET','POST'])
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        print(request.form)
        connection = sqlite3.connect("user_data.db")
        cursor = connection.cursor()

        username = request.form['username']
        password = request.form['password']

        print(f"values are: {(username, password)}")

        sql = f"SELECT * FROM users WHERE name = '{ username }' AND password = '{ password }'"
        cursor.execute(sql)

        results = cursor.fetchone()

        if not None:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('fast_trade_home'))

        else:
            flash("User not found !")
            return render_template('auth/login.html')

    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash("Log out, see you!")
    return render_template('auth/login.html')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()