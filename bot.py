import os

import telegram
from environs import Env
from google.cloud import dialogflow
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler, Updater


def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

    return response


def start(update: Update, context: CallbackContext) -> None:
    notification = 'Здравствуйте'
    update.message.reply_text(text=notification)


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def dialogflow_handle(update: Update, context: CallbackContext) -> None:
    env = Env()
    env.read_env()
    texts = [update.message.text]
    session_id = [update.message.chat_id]

    response = detect_intent_texts(
        project_id=env('PROJECT_ID'),
        session_id=session_id,
        texts=texts,
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
