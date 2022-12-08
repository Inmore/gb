# 3. Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.
def get_unique_items(items):
    return list(filter(lambda i: items.count(i) == 1 in items, items))


print(get_unique_items([5, 5, 7, 9, 2, 1, 2]))
