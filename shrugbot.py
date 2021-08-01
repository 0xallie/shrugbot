#!/usr/bin/env python3

import argparse
import logging
import uuid

import toml
from telegram import Bot, InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import CallbackContext, InlineQueryHandler, Updater


def on_inline_query(update: Update, context: CallbackContext) -> None:
    text = fr'{update.inline_query.query} ¯\_(ツ)_/¯'

    update.inline_query.answer([
        InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title=text,
            input_message_content=InputTextMessageContent(text),
        ),
    ])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', help='enable debug logging')
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    )

    config = toml.load('config.toml')

    bot = Bot(config['token'])

    updater = Updater(bot=bot)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(InlineQueryHandler(on_inline_query))

    updater.start_polling()
    updater.idle()
