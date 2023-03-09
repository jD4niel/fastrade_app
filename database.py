# Imports / Setup
import sqlite3
connection = sqlite3. connect("user_data.db")
cursor = connection.cursor()
#
# Queries
command = "CREATE TABLE IF NOT EXISTS users (name TEXT, password TEXT)"
cursor.execute(command)
cursor.execute("INSERT INTO users VALUES ('admin', '1234')")

connection.commit()
