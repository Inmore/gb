# 3.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
def pair_multiply(input_list):
    count = len(input_list)
    return [input_list[item] * list(reversed(input_list))[item] for item in range(math.ceil(count / 2))]


print(pair_multiply([2, 3, 4, 5, 6]))
