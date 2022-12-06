# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# *Пример:*
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8)
# Fn = F(n+2)−F(n+1).
# Они также могут быть определены по формуле F−n = (−1)**(n+1)*Fn.
def fibo(num):
    if num == 0:
        result = 0
        return result
    elif num == 1 or num == 2:
        result = 1
        return result
    elif num < 0:
        result = fibo(num + 2) - fibo(num + 1)
        return result
    else:
        result = fibo(num - 1) + fibo(num - 2)
        return result


def get_fibo_list(num):
    list_fibo = []
    for i in range(-num, num + 1):
        list_fibo.append(fibo(i))
    return list_fibo


print(get_fibo_list(8))
