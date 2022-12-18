import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import hi_command, time_command, help_command, sum_command, sub_command, csum_command, \
    mult_command, div_command, csub_command, cmult_command, cdiv_command, fsum_command, fsub_command, fmult_command, fdiv_command
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('tg_token')
updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))

# integer
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('sub', sub_command))
updater.dispatcher.add_handler(CommandHandler('mult', mult_command))
updater.dispatcher.add_handler(CommandHandler('div', div_command))

# complex
updater.dispatcher.add_handler(CommandHandler('csum', csum_command))
updater.dispatcher.add_handler(CommandHandler('csub', csub_command))
updater.dispatcher.add_handler(CommandHandler('cmult', cmult_command))
updater.dispatcher.add_handler(CommandHandler('cdiv', cdiv_command))

# fractions
updater.dispatcher.add_handler(CommandHandler('fsum', fsum_command))
updater.dispatcher.add_handler(CommandHandler('fsub', fsub_command))
updater.dispatcher.add_handler(CommandHandler('fmult', fmult_command))
updater.dispatcher.add_handler(CommandHandler('fdiv', fdiv_command))

print('server start')
updater.start_polling()
updater.idle()