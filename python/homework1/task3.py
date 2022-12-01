# 3. Вывести на экран числа от -N до N.
def print_numbers():
    number = int(input('Введите натуральное число: '))
    min_val = -number
    max_val = number + 1
    for number in range(min_val, max_val):
        print(number)


print_numbers()