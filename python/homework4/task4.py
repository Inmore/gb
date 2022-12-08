import random


# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
#         *Пример:*
#
#         - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
def write_polynomial_to_file(k):
    f = open('file1.txt', 'w', encoding='utf-8')
    k_dict = {i: random.randint(0, 100) for i in range(k + 1)}
    result = ''
    for key, val in reversed(k_dict.items()):
        result = result + str(val) + '*x' + '^' + str(key)
        if key != 0:
            result += ' + '
    result += ' = 0'
    f.write(result)
    f.close()


write_polynomial_to_file(3)
