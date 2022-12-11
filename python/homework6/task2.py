# 2.Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6:
#     [2.0, 2.25, 2.3704, 2.4414, 2.4883, 2.5216]
#     Сумма чисел = 14.0717
def chain_sum():
    number = int(input('Введите натуральное число: '))
    chain = [round((1 + 1 / (i + 1)) ** (i + 1), 4) for i in range(number)]
    print(chain)
    return sum(chain)


print(chain_sum())
