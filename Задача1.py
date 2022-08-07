#Вычислить число pi c заданной точностью d Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math


def find_numbers_of_pi(user_number: str):
    return len(user_number) - 2


print('Программа высчитывает число "pi" с заданной точностью')
number = input('Введите точность расчета в виде вещественного числа: ')
print(f'π = {round(math.pi, find_numbers_of_pi(number))}')