from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, ParseMode
from telegram.ext import ConversationHandler

MODE, DIM_CHOICE, INPUT_RESULT, CONV, CONV_INPUT = range(5)


def get_recommendation_command(x):
    if x < 20:
        reply_text = "\n*Дефицит витамина D*\n\n"
        recommended_dose_text = "После консультации с врачом можно выбрать одну из следующих схем лечения:\n\n"
        recommended_dose_text += "• 50 000 МЕ еженедельно в течение 8 недель внутрь\n"
        recommended_dose_text += "• 200 000 МЕ ежемесячно в течение 2 месяцев внутрь\n"
        recommended_dose_text += "• 150 000 МЕ ежемесячно в течение 3 месяцев внутрь\n"
        recommended_dose_text += "• 6 000 – 8 000 МЕ в день – 8 недель внутрь\n\n"
        recommended_dose_text += "После окончания курса лечения рекомендуется повторно сдать " \
                                 "анализ крови на содержание 25 (OH)D.\n\n"
    elif x < 30:
        reply_text = "\n*Недостаточность витамина D*\n\n"
        recommended_dose_text = "После консультации с врачом можно выбрать одну из следующих схем лечения:\n\n"
        recommended_dose_text += "• 50 000 МЕ еженедельно в течение 4 недель внутрь\n"
        recommended_dose_text += "• 200 000 МЕ однократно внутрь\n"
        recommended_dose_text += "• 150 000 МЕ однократно внутрь\n"
        recommended_dose_text += "• 6 000 – 8 000 МЕ в день – 4 недели внутрь\n\n"
        recommended_dose_text += "После окончания курса лечения рекомендуется повторно сдать " \
                                 "анализ крови на содержание 25 (OH)D.\n\n"
    elif x < 100:
        reply_text = "\n*Нормальное содержание витамина D*\n\n"
        recommended_dose_text = "После консультации с врачом, можно выбрать одну из следующих схем профилактики:\n\n"
        recommended_dose_text += "• 1 000 – 2 000 МЕ ежедневно внутрь\n"
        recommended_dose_text += "• 6 000 – 14 000 МЕ однократно в неделю внутрь\n\n"
    else:
        reply_text = "\n*Повышенный уровень витамина D*\n\n"
        recommended_dose_text = "Требуется обратиться за консультацией к врачу и провести " \
                                "дополнительное исследование уровня кальция в крови.\n\n"
    return f'{reply_text}{recommended_dose_text}'


def ng_ml_to_nmol_l(ng_ml: float) -> float:
    return round(ng_ml * 2.496, 3)


def nmol_l_to_ng_ml(nmol_l: float) -> float:
    return round(nmol_l / 2.496, 3)


def mkg_to_me(mkg: float) -> float:
    return round(mkg * 40, 3)


def start(update, _):
    reply_keyboard = [['Рассчитать дозу', 'Перевод единиц измерения']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Привет. \n\n'
        'Перед началом приема витамина D3 важно проконсультироваться с врачом, '
        'т.к. дозировка и схема лечения могут различаться в зависимости от вашего '
        'здоровья и потребностей. \n\n'
        'Команда /cancel, чтобы прекратить разговор.\n\n'
        'Что вы хотите сделать?',
        reply_markup=markup_key, )
    return MODE


def cancel(update, _):
    update.message.reply_text(
        'Начать сначала /start',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


def mode_handler(update, _):
    res = ConversationHandler.END
    if update.message.text == 'Рассчитать дозу':
        reply_keyboard = [['нмоль/л', 'нг/мл']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text(
            'Выберите, в каких единицах Ваш результат анализа: ',
            reply_markup=markup_key,
        )
        res = DIM_CHOICE
    if update.message.text == 'Перевод единиц измерения':
        reply_keyboard = [['нмоль/л -> нг/мл', 'нг/мл -> нмоль/л', 'мкг -> МЕ']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text(
            'Выберите нужный режим перевода единиц измерения: ',
            reply_markup=markup_key,
        )
        res = CONV
    return res


def dim_choice(update, _):
    context = _
    context.user_data['dim'] = update.message.text
    update.message.reply_text(
        'Введите Ваш результат анализа: ',
        reply_markup=ReplyKeyboardRemove(),
    )
    return INPUT_RESULT


def input_result(update, _):
    context = _
    txt = update.message.text
    try:
        x = float(txt)
        if context.user_data['dim'] == 'нмоль/л':
            x = nmol_l_to_ng_ml(x)
        res = get_recommendation_command(x)
        update.message.reply_text(
            f'Ваш результат: {res}'
            'Начать сначала /start',
            reply_markup=ReplyKeyboardRemove(),
            parse_mode=ParseMode.MARKDOWN
        )
    except ValueError:
        update.message.reply_text(
            f'Введите число!\n'
            'Начать сначала /start',
            reply_markup=ReplyKeyboardRemove()
        )
    return ConversationHandler.END


def conv_handler(update, _):
    context = _
    res = ConversationHandler.END
    if update.message.text:
        context.user_data['conv'] = update.message.text
        res = CONV_INPUT
    return res


def input_conv(update, _):
    context = _
    conv = context.user_data['conv']
    txt = update.message.text
    try:
        x = float(txt)
        if conv == 'нмоль/л -> нг/мл':
            res = nmol_l_to_ng_ml(x)
            dim = 'нг/мл'
        elif conv == 'мкг -> МЕ':
            res = mkg_to_me(x)
            dim = 'ME'
        else:
            res = ng_ml_to_nmol_l(x)
            dim = 'нмоль/л'
        update.message.reply_text(
            f'Результат: {res} {dim}.\n\n'
            'Начать сначала /start',
            reply_markup=ReplyKeyboardRemove()
        )
    except ValueError:
        update.message.reply_text(
            f'Введите число!\n\n'
            'Начать сначала /start',
            reply_markup=ReplyKeyboardRemove()
        )
    return ConversationHandler.END
