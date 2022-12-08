# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def get_simple_multipliers(number):
    multipliers = []
    i = 2
    while i * i <= number:
        while number % i == 0:
            multipliers.append(i)
            number = int(number / i)
        i += 1
    if number > 1:
        multipliers.append(number)
    return multipliers


print(get_simple_multipliers(12))
