# 1.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def multiply_list():
    number = int(input('Введите натуральное число: '))
    return [fact(i + 1) for i in range(number)]


def fact(number):
    temp = 1
    for sub_item in range(number):
        temp *= sub_item + 1
    return temp


print(multiply_list())
