import os

import telegram
from environs import Env
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler, Updater

from api import detect_intent_texts


def start(update: Update, context: CallbackContext) -> None:
    notification = 'Здравствуйте'
    update.message.reply_text(text=notification)


def dialogflow_handle(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    session_id = [update.message.chat_id]
    response = detect_intent_texts(
        project_id=os.environ['PROJECT_ID'],
        session_id=session_id,
        text=text,
        language_code='ru'
    )
    update.message.reply_text(response.query_result.fulfillment_text)


def main() -> None:
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])
    updater = Updater(bot=bot, use_context=True)

    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, dialogflow_handle))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
