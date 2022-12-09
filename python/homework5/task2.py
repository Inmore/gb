import random


# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
# ход друг после друга. Первый ход определяется жеребьёвкой. За один ход
# можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
# сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
def step(count, number):
    return count - number


def run(bot=False):
    max_num = 28
    start_count = 121
    count = start_count
    total = 0
    player = ''
    is_bot = False
    i = 0

    while count > 0:

        if i % 2 == 0:
            player = 'A'
            if bot:
                is_bot = False
        else:
            player = 'B'
            if bot:
                is_bot = True

        if not is_bot:
            step_count = int(input(f'Игрок {player}, введите, сколько конфет от 1 до {max_num} вы желаете забрать: '))
        else:
            step_count = random.randint(1, max_num)
            if start_count - max_num * 2 - 1 <= total < start_count - max_num - 1:
                step_count = start_count - total - max_num - 1
            if start_count - max_num < total:
                step_count = start_count - total

        if total + step_count > start_count:
            step_count = start_count - total
        total += step_count
        count = step(count, step_count)

        print(f'Сходил игрок {player}. Осталось {count} конфет. Всего конфет забрано обоими игроками {total}.')
        i += 1
    print(f'--- Победил игрок {player}! ---')


run(True)
