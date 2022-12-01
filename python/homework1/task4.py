# 4. Показать первую цифру дробной части числа.
def show_frac_first_figure():
    value = float(input('введите число: '))
    frac_part = value - int(value)
    result = int(frac_part * 10)
    print(result)


show_frac_first_figure()