# 1.Напишите программу, которая принимает на вход цифру, обозначающую день
# недели, и проверяет, является ли этот день выходным.
#
# *Пример:*
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет
def is_weekend():
    day_number = int(input('Введите день недели: '))
    result = 'нет'
    if day_number in range(1, 8):
        if day_number == 6 or day_number == 7:
            result = 'да'
    else:
        result = 'нет дня недели с таким номером'
    return result


print(is_weekend())