import os

import telegram
from environs import Env
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler, Updater


def start(update: Update, context: CallbackContext) -> None:
    notification = 'Здравствуйте'
    update.message.reply_text(text=notification)


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main() -> None:
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])
    updater = Updater(bot=bot, use_context=True)

    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
