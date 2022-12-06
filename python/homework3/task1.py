# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# *Пример:*
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def odd_position_items_sum(input_list):
    filtered_list = list(filter(lambda x: x[0] % 2 != 0, enumerate(input_list)))
    return sum(map(lambda x: x[1], filtered_list))


test_list = [2, 3, 5, 9, 3]


print(odd_position_items_sum(test_list))