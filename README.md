# FasTrading 
##### _a cool library to make good trading entries_

Fastrading is a simple library that makes trading entries using MACD, RSI and ✨Magic ✨

## Features

- get_symbols (usdt,busd,all symbols)
- do a fast_trade


> This library still on progress now im doing some testing
> not working! :P



## Installation

requirements.txt to install all libraries


```sh
pip install -r requirements.txt
```

Add **YOUR** environment variables for BINANCE and TELEGRAM

```sh
export BINANCE_API_KEY='asdfghjkl';
export BINANCE_API_SECRET='asdfghjkl';
export TELEGRAM_CHAT_ID="234567890";
export TELEGRAM_TOKEN="qwertyuiop";
```

## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| GitHub | [plugins/github/README.md][PlGh] |

## tmux 
Fastrading creates a tmux session, with a window for each trade

here is basic commands for tmux:

|Key Binding | Command | Explanation |
| ------ | ------ | ------ |
| Ctrl-b ? | tmux list-keys |   Display a list of all key bindings |
| Ctrl-b c | tmux new-window |  Create a new window |
| Ctrl-b , | tmux rename-window |   Rename the current window |
| Ctrl-b n | tmux select-window | -n    Switch to the next window |
| Ctrl-b p | tmux select-window | -p    Switch to the previous window |
| Ctrl-b & | tmux kill-window | Kill the current window |
| Ctrl-b % | tmux split-window | -h Split the current pane horizontally |
| Ctrl-b " | tmux split-window | -v Split the current pane vertically |
| Ctrl-b o | tmux select-pane | -t :.+| Move to the next pane |
| Ctrl-b ; | tmux last-pane |   Move to the last active pane |

## Development

Want to contribute? Great!



