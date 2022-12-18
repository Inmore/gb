import math


# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# *Пример:*
#
# - 6782 -> 23
# - 0,56 -> 11
def sum_digits(r_num: float):
    sum_digs = 0

    for part in math.modf(r_num):
        part = round(part, 10)
        for d in str(part):
            if d.isdigit():
                sum_digs += int(d)

    return sum_digs


# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30.
def check_number(number: int):
    if number % 5 == 0 and ((number % 10 == 0 or number % 15 == 0) and number % 30 != 0):
        return 'yes'
    else:
        return 'no'
