from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext


def hi_command(update: Update, context: CallbackContext):
    btn1 = InlineKeyboardButton(text='Рассчитать дозу витамина D', callback_data='calculate_dose_btn')
    btn2 = InlineKeyboardButton(text='Перевести нг/мл в нмоль/л', callback_data='ng_ml_to_nmol_l')
    btn3 = InlineKeyboardButton(text='Перевести нмоль/л в нг/мл', callback_data='nmol_l_to_ng_ml')
    markup = InlineKeyboardMarkup([[btn1, btn2, btn3]])
    update.message.reply_text(f'Приветствуем Вас, {update.effective_user.first_name}! Чтобы бы Вы хотели сделать?', reply_markup=markup)


def get_recommendation_command(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    reply_text = ''
    recommended_dose_text = 'Не удалось подобрать рекомендацию'
    if x < 20:
        reply_text = "Дефицит витамина D\n"
        recommended_dose_text = "50 000 МЕ еженедельно в течение 8 недель внутрь\n"
        recommended_dose_text += "200 000 МЕ ежемесячно в течение 2 месяцев внутрь\n"
        recommended_dose_text += "150 000 МЕ ежемесячно в течение 3 месяцев внутрь\n"
        recommended_dose_text += "6 000 – 8 000 МЕ в день – 8 недель внутрь\n"
    elif x < 30:
        reply_text = "Недостаточность витамина D\n"
        recommended_dose_text = "50 000 МЕ еженедельно в течение 4 недель внутрь\n"
        recommended_dose_text += "200 000 МЕ однократно внутрь\n"
        recommended_dose_text += "150 000 МЕ однократно внутрь\n"
        recommended_dose_text += "6 000 – 8 000 МЕ в день – 4 недели внутрь\n"
    elif x < 100:
        reply_text = "Адекватный уровень витамина D\n"
        recommended_dose_text = "Поддерживающие профилактические дозы витамина D\n"
        recommended_dose_text += "1 000 – 2 000 МЕ ежедневно внутрь\n"
        recommended_dose_text += "6 000 – 14 000 МЕ однократно в неделю внутрь\n"
    update.message.reply_text(f'{reply_text}{recommended_dose_text}')


def ng_ml_to_nmol_l(ng_ml: float) -> float:
    return round(ng_ml * 2.496, 3)


def nmol_l_to_ng_ml(nmol_l: float) -> float:
    return round(nmol_l / 2.496, 3)


def callback_handler(update, context):
    query = update.callback_query
    pass


