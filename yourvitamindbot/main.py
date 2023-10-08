import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from bot_commands import hi_command, get_recommendation_command, callback_handler
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('tg_token')
updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CallbackQueryHandler(callback_handler))
updater.dispatcher.add_handler(CommandHandler('vitamin', get_recommendation_command))

print('server start')
updater.start_polling()
updater.idle()