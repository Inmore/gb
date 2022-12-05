# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение
# элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
def multiply_with_positions_from_file():
    number = int(input('Введите натуральное число: '))
    n_list = list(range(-number, number + 1))
    positions = []
    f = open('file.txt', 'r', encoding='utf-8')
    lines = f.readlines()

    for line in lines:
        positions.append(int(line))
    result = 0

    for position in positions:
        if position < len(n_list):
            result += n_list[position]

    return result


print(multiply_with_positions_from_file())
