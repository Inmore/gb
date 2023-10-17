import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from bot_commands import start, cancel, MODE, \
    mode_handler, DIM_CHOICE, dim_choice, INPUT_RESULT, input_result, CONV, conv_handler, CONV_INPUT, input_conv
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('tg_token')
updater = Updater(TOKEN)

updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        MODE: [MessageHandler(Filters.regex('^(Рассчитать дозу|Перевод единиц измерения)$'), mode_handler)],
        DIM_CHOICE: [MessageHandler(Filters.regex('^(нмоль/л|нг/мл)$'), dim_choice)],
        INPUT_RESULT: [MessageHandler(Filters.text, input_result)],
        CONV: [MessageHandler(Filters.regex('^(нмоль/л -> нг/мл|нг/мл -> нмоль/л|мкг -> МЕ)$'), conv_handler)],
        CONV_INPUT: [MessageHandler(Filters.text, input_conv)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
))

print('server start')
updater.start_polling()
updater.idle()
