import math

# 3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# *Пример:*
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def frac_diff(real_list):
    frac_list = list(map(lambda i: round(math.modf(i)[0], 5), real_list))
    min_val = min(filter(lambda i: i != 0, frac_list))
    max_val = max(filter(lambda i: i != 0, frac_list))
    return max_val - min_val


print(frac_diff([1.1, 1.2, 3.1, 5, 10.01]))