import math


# 1. Вычислить число c заданной точностью d
#
#         *Пример:*
#
#         - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
def calc(num, pre):
    if 1e-10 <= pre <= 0.1:
        pre = abs(int(round(math.log10(pre))))
    else:
        pre = 1
    return round(num, pre)


print(calc(math.pi, 0.001))
