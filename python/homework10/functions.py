import math


# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# *Пример:*
#
# - 6782 -> 23
# - 0,56 -> 11
def sum_digits(r_num: float):
    sum_digs = 0

    for part in math.modf(r_num):
        part = round(part, 10)
        for d in str(part):
            if d.isdigit():
                sum_digs += int(d)

    return sum_digs


# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30.
def check_number(number: int):
    if number % 5 == 0 and ((number % 10 == 0 or number % 15 == 0) and number % 30 != 0):
        return 'yes'
    else:
        return 'no'

def by_one_gram(val: float):
    return val / 100


def bgu(result_food, target_e=330, name='product'):
    k = 1
    t_e = 0
    t_b = 0
    t_g = 0
    t_u = 0
    result_k = 1

    while t_e < target_e:
        t_e = 0
        t_b = 0
        t_g = 0
        t_u = 0
        for food_name, mult in result_food.items():
            t_b += k * mult * by_one_gram(food[food_name]['b'])
            t_g += k * mult * by_one_gram(food[food_name]['g'])
            t_u += k * mult * by_one_gram(food[food_name]['u'])
            t_e += k * mult * by_one_gram(food[food_name]['e'])
        result_k = k
        k *= 1.01

    sum_mass = 0
    for food_name, mul in result_food.items():
        ingredient_mass = round(result_k * mul, 2)
        sum_mass += ingredient_mass
        print(f'{food_name}: {ingredient_mass} g')

    print(f'Выход {round(sum_mass, 2)} g')

    print(round(t_b, 2), round(t_g, 2), round(t_u, 2), round(t_e, 2))
    print(t_b)
    print(t_b / t_b, round(t_g / t_b, 2), round(t_u / t_b, 2))

    return


class Bgue:
    def __init__(self, b: float, g: float, u: float, e: float):
        self.b = b
        self.g = g
        self.u = u
        self.e = e


# products = [
#     {'name': 'gre', 'bgue': Bgue(12, 3.4, 72, 335.4)},
#     {'name': 'sem', 'bgue': Bgue(20.7, 52.9, 10.5, 600.9)},
# ]
# print(products)
food = {
        'gre': {'b': 12.0, 'g': 3.4, 'u': 72.0, 'e': 335.4},
        'sem': {'b': 20.7, 'g': 52.9, 'u': 10.5, 'e': 600.9},
        'sha': {'b': 10.7, 'g': 1.0, 'u': 73.0, 'e': 355.8},
        'izu': {'b': 2.9, 'g': 0.5, 'u': 67.0, 'e': 284.1},
        'chernosliv': {'b': 2.3, 'g': 0, 'u': 58.4, 'e': 242},
        'kish': {'b': 11.1, 'g': 15.9, 'u': 19.5, 'e': 265.5},
        'tom': {'b': 0.9, 'g': 0.2, 'u': 3.9, 'e': 18},
        'smetana15': {'b': 2.5, 'g': 15, 'u': 3.6, 'e': 160},
        'smetana20': {'b': 2.5, 'g': 20, 'u': 3.4, 'e': 203.6},
        'baton': {'b': 6.9, 'g': 1.1, 'u': 50, 'e': 237.5},
        'maslo': {'b': 1.3, 'g': 61.5, 'u': 1.9, 'e': 566.3},
        'yayca': {'b': 12.7, 'g': 11.5, 'u': 0.7, 'e': 155.9},
        'syrok_kakao': {'b': 15.0, 'g': 11.0, 'u': 34.0, 'e': 295},
        'tvorog5': {'b': 16.0, 'g': 5.0, 'u': 3.0, 'e': 121},
        'tvorozhok5': {'b': 3, 'g': 2.5, 'u': 10.4, 'e': 76.1},
        'muka1s': {'b': 10.6, 'g': 1.3, 'u': 69, 'e': 330.1},
        'kart': {'b': 2.0, 'g': 0.4, 'u': 16.3, 'e': 77},
        'syr': {'b': 25.9, 'g': 27.1, 'u': 2.1, 'e': 355.9},
        'grec': {'b': 14.8, 'g': 64, 'u': 13.7, 'e': 698},
        'gerkules': {'b': 12.0, 'g': 6.0, 'u': 62, 'e': 350},
        'sok_ya_mor': {'b': 0.0, 'g': 0.0, 'u': 10, 'e': 40},
        'lepeshka': {'b': 12.7, 'g': 14.6, 'u': 24.5, 'e': 280.2},
        'hlebcy_grech': {'b': 10.5, 'g': 5.4, 'u': 78.6, 'e': 387.0},
        'struzhka_kokos': {'b': 13, 'g': 62, 'u': 14, 'e': 666.0},
        'shok_mol': {'b': 7, 'g': 31.8, 'u': 57.4, 'e': 543.8},
        'shok_85': {'b': 10.3, 'g': 41.7, 'u': 42.8, 'e': 587.7},
        'moloko32': {'b': 3, 'g': 3.2, 'u': 4.7, 'e': 60},
        'moloko25': {'b': 3, 'g': 2.5, 'u': 4.7, 'e': 53.3},
        'moloko1': {'b': 3, 'g': 1, 'u': 4.7, 'e': 39.8},
        'slivki10': {'b': 2.6, 'g': 10, 'u': 4.5, 'e': 118},
        'kefir32': {'b': 3, 'g': 3.2, 'u': 4.0, 'e': 57},
        'kakao_poroshok': {'b': 28, 'g': 12, 'u': 29.8, 'e': 339.2},
        'sahar': {'b': 0, 'g': 0, 'u': 100, 'e': 400},
        'voda': {'b': 0, 'g': 0, 'u': 0, 'e': 0},
        'banan': {'b': 1.09, 'g': 0.33, 'u': 22.84, 'e': 89},
        'plombir': {'b': 4.2, 'g': 14.6, 'u': 22.3, 'e': 237},
        'makarony': {'b': 12, 'g': 1.3, 'u': 73, 'e': 358},
        'mayonez': {'b': 0.4, 'g': 67, 'u': 2.1, 'e': 613},
        'zefir': {'b': 2, 'g': 10.3, 'u': 62, 'e': 348.7},
        'xxx': {'b': 12, 'g': 0, 'u': 0, 'e': 300},
        'null': {'b': 0, 'g': 0, 'u': 0, 'e': 0},
    }

# печенье с творогом 5%
# result_food = {'muka1s': 4, 'tvorog5': 2, 'maslo': 1, 'yayca': 2}
# творог с изюмом и сметаной
# result_food = {'tvorog5': 1, 'izu': 1, 'smetana15': 1}
# гречка с семечками
result_food = {'sem': 1, 'gre': 3}
# отруби с семечками
# result_food = {'sem': 1, 'sha': 3.5, 'tvorog5': 1}
# отруби с молоком
# result_food = {'sem': 0.6, 'sha': 3.5, 'moloko32': 12.5}
# яйца с изюмом
# result_food = {'yayca': 1, 'izu': 1}
# яйца с черносливом
# result_food = {'yayca': 1, 'chernosliv': 0.9}
# батон с маслом и творогом 5%
# result_food = {'baton': 5, 'maslo': 1, 'tvorog5': 3}
# картофель с сыром
# result_food = {'kart': 30, 'maslo': 1, 'syr': 3}
# картофельное пюре
# result_food = {'kart': 1, 'maslo': 0.04, 'moloko32': 1.1}
# гречка с семечками и сыром
# result_food = {'gre': 7, 'syr': 1, 'sem': 2}
# гречка с грецкими орехами и сыром
# result_food = {'gre': 6, 'grec': 1, 'syr': 1}
# геркулес с семечками
# result_food = {'gerkules': 5, 'sem': 1} # 330
# киш с соком яблочно-морковным
# result_food = {'kish': 1, 'sok_ya_mor': 1.25} # 500
# лепешка с соком яблочно-морковным
# result_food = {'lepeshka': 1, 'sok_ya_mor': 1.74} # 400
# сырок с какао с яблочно-морковным соком
# result_food = {'syrok_kakao': 1, 'sok_ya_mor': 1.4} # 500
# сырок с какао с яблочно-морковным соком и гречневыми хлебцами (сырок 3 шт, сок 1 шт, хлебцы 1 шт)
# result_food = {'syrok_kakao': 4, 'sok_ya_mor': 6.7, 'hlebcy_grech': 1} # 548
# Творог с изюмом и кокосовой стружкой
# result_food = {'struzhka_kokos': 1, 'izu': 5, 'tvorog5': 4} #
# гречневые хлебцы с творогом 5% и молочным шоколадом
# result_food = {'shok_mol': 1, 'tvorog5': 2, 'hlebcy_grech': 1} # 360
# какао-напиток со сливками
# result_food = {'kakao_poroshok': 1, 'slivki10': 1.5, 'sahar': 0.8, 'voda': 25} # 90
# какао-напиток со сливками
# result_food = {'kakao_poroshok': 2, 'moloko32': 5, 'sahar': 1.6, 'voda': 25} # 90
# какао-напиток с молоком
# result_food = {'kakao_poroshok': 1, 'slivki10': 0.5, 'sahar': 1.4, 'voda': 39, 'moloko32': 10} # 90
# творог с изюмом и сметаной
# result_food = {'tvorog5': 1.3, 'izu': 1.3, 'smetana20': 1}
# коктейль без пломбира
# result_food = {'banan': 2.5, 'moloko32': 9} # 410 (банан 1 шт. + 0,5 л молока)
# коктейль с пломбиром
# result_food = {'plombir': 1, 'moloko1': 5, 'banan': 1}
# макароны с яйцами и майонезом
# result_food = {'mayonez': 1, 'makarony': 6, 'yayca': 3}
# кефир с черносливом и творогом
# result_food = {'kefir32': 7, 'tvorog5': 0, 'zefir': 1, 'voda': 0} # 90
# result_food = {'smetana20': 5, 'sha': 1, 'sem': 0, 'voda': 0} # 90
# result_food = {'kish': 1, 'sok_ya_mor': 1.25, 'tvorozhok5': 1.25} # 90
bgu(result_food, 330)

print('ref', 37.5/37.5, round(33.3/37.5, 2), round(137.5/37.5, 2))

