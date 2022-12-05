# 3.Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.
#
# *Пример:*
#
# - Для n = 6:
#     [2.0, 2.25, 2.3704, 2.4414, 2.4883, 2.5216]
#     Сумма чисел = 14.0717
def chain_sum():
    number = int(input('Введите натуральное число: '))
    chain = []
    for i in range(number):
        chain.append(round((1 + 1 / (i + 1)) ** (i + 1), 4))
    print(chain)
    result = 0
    for item in chain:
        result += item
    return result


print(chain_sum())