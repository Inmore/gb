# 2. Найти максимальное из пяти чисел.
def max_num():
    print('введите 5 целых чисел')
    numbers = []
    for number in range(5):
        numbers.append(int(input()))
    max_temp = numbers[0]
    for number in numbers:
        if number > max_temp:
            max_temp = number
    print(f'max: {max_temp}')


max_num()    