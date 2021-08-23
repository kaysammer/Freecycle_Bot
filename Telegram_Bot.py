from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello command received")
    print("Hello command received and replied to")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)

updater.start_polling()

for x in "banana":
    context.bot.send_message(chat_id=update.effective_chat.id, text=x)
