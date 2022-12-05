import random


# 5.Реализуйте алгоритм перемешивания списка.
def mix_list(input_list):
    rand_index = random.randint(0, len(input_list) - 1)
    for idx, value in enumerate(input_list):
        if idx != rand_index:
            temp = input_list[idx]
            input_list[idx] = input_list[rand_index]
            input_list[rand_index] = temp
    return input_list


print(mix_list([1, 2, 3, 4, 5]))