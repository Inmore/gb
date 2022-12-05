# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# *Пример:*
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def multiply_list():
    number = int(input('Введите натуральное число: '))
    result = []
    for item in range(number):
        temp = 1
        for sub_item in range(item + 1):
            temp *= sub_item + 1
        result.append(temp)
    return result


print(multiply_list())