# 3. Создайте программу для игры в ""Крестики-нолики"".
def print_list(in_list):
    for i in in_list:
        print(i)


def check_win(in_list):

    # Все по горизонтали

    for i_idx, iv in enumerate(in_list):
        x, y, z = ['', '', '']
        for j_idx, jv in enumerate(iv):
            if j_idx == 0:
                x = iv[j_idx]
            if j_idx == 1:
                y = iv[j_idx]
            if j_idx == 2:
                z = iv[j_idx]
        if x == y == z:
            return True

    # По вертикали
    x, y, z = ['', '', '']
    for item in range(3):
        for i_idx, iv in enumerate(in_list):
            if i_idx == 0:
                x = iv[item]
            if i_idx == 1:
                y = iv[item]
            if i_idx == 2:
                z = iv[item]
        if x == y == z:
            return True

    # По диагонали

    x, y, z = ['', '', '']
    for i_idx, iv in enumerate(in_list):
        if i_idx == 0:
            x = iv[i_idx]
        if i_idx == 1:
            y = iv[i_idx]
        if i_idx == 2:
            z = iv[i_idx]
    if x == y == z:
        return True

    for i_idx, iv in enumerate(in_list):
        if i_idx == 0:
            x = iv[2 - i_idx]
        if i_idx == 1:
            y = iv[2 - i_idx]
        if i_idx == 2:
            z = iv[2 - i_idx]
    if x == y == z:
        return True

    return False


def game():
    a = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
    ]
    k = 0

    for item in range(9):
        if k % 2 == 0:
            player = 'A'
            cell = int(input('введите номер ячейки для установки крестика: '))
            for i_idx, iv in enumerate(a):
                for j_idx, jv in enumerate(iv):
                    if jv.isdigit():
                        if cell == int(jv) and cell != 'x' and cell != '0':
                            a[i_idx][j_idx] = 'x'
        else:
            player = 'B'
            cell = int(input('введите номер ячейки для установки нолика: '))
            for i_idx, iv in enumerate(a):
                for j_idx, jv in enumerate(iv):
                    if jv.isdigit():
                        if cell == int(jv) and cell != 'x' and cell != '0':
                            a[i_idx][j_idx] = '0'
        k += 1
        print_list(a)
        if check_win(a):
            print(f'Победил игрок {player}!')
            break;


game()
