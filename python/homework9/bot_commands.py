from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/help')


def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')


def sub_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} - {y} = {x-y}')


def mult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} * {y} = {x*y}')


def div_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} * {y} = {round(x/y, 2)}')


def csum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')


def csub_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} - {y} = {x-y}')


def cmult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} * {y} = {x*y}')


def cdiv_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} / {y} = {x/y}')
