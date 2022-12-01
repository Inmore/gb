# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30.
def check_number():
    number = int(input('введите число для проверки его кратности 5 и 10 или 15, но не 30: '))
    if number % 5 == 0 and ((number % 10 == 0 or number % 15 == 0) and number % 30 != 0):
        print('подходит')
    else:
        print('не подходит')


check_number()
