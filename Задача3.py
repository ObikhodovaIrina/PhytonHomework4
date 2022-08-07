# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random


def fill_list(min_number=0, max_number=9, length=0):
    new_list = []
    for i in range(length):
        new_list.append(random.randint(min_number, max_number))
    return new_list


user_length = int(input('Введите длину последовательности: '))
my_list = fill_list(length=user_length)
print(f'Начальная последовательность ---> {my_list}')
my_set = list(set(my_list))
print(f'Неповторяющиеся элементы последовательности ---> {my_set}')