# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# *Пример:*
#
# - 6782 -> 23
# - 0,56 -> 11
import math


def sum_digits():
    number = float(input('Введите вещественное число: '))
    sum_digs = 0

    for part in math.modf(number):
        part = round(part, 10)
        for d in str(part):
            if d.isdigit():
                sum_digs += int(d)

    print(sum_digs)


sum_digits()