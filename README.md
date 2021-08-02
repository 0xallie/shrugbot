# Shrug Bot

A simple Telegram bot to send the shrug (¯\\_(ツ)_/¯) emote to any chat – a replacement of the old `@ShrugBot`.

## Usage

Send `@ShrugRobot [text]` in any Telegram chat, and the shrug emote will be appended to whatever text you write. (You don't have to write anything, you can also just send a shrug by itself.)

## Installation

If you want to self-host the bot, here are the steps to do so:

* Install Python 3.6 or newer
* Install the dependencies via `poetry install` or `pip install -r requirements.txt`
* Create a bot via BotFather and enable inline mode
* Copy `config.toml.example` to `config.toml` and fill in the token you got from BotFather
* Start the bot with `./shrugbot.py`
