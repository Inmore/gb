# 4.Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).
def coords_range(quarter_num):
    if quarter_num == 1:
        result = 'x > 0, y > 0'
    elif quarter_num == 2:
        result = 'x < 0, y > 0'
    elif quarter_num == 3:
        result = 'x < 0, y < 0'
    elif quarter_num == 4:
        result = 'x > 0, y < 0'
    else:
        result = f'Нет четверти с номером {quarter_num}'
    return result


print(coords_range(1))