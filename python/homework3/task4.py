# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# *Пример:*
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def dec_to_bin():
    dec = int(input('Введите целое число: '))
    result = ''
    minus = ''
    if dec < 0:
        dec = -dec
        minus = '-'
    if dec == 0:
        result = 0
    while dec > 0:
        result = str(dec % 2) + result
        dec //= 2
    print(minus + result)


dec_to_bin()