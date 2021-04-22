"""

Задача №3.
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

"""
# принципиально не хочу функцию index
import random

first_array = [random.randint(0, 101) for i in range(15)]
result = list.copy(first_array)

revert_array = []
print(f'Сгенерировали список: {first_array}')

while first_array != []:
    for index in range(len(first_array) - 1):
        if first_array[index] > first_array[index + 1]:
            first_array[index], first_array[index + 1] = first_array[index + 1], first_array[index]
    if first_array != []:
        revert_array.extend([first_array.pop(len(first_array) - 1)])
print(f'Отсортировали по убыванию: {revert_array}')


for index in range(len(result)):
    if result[index] == revert_array[len(revert_array) - 1]:
        result[index] = revert_array[0]
    elif result[index] == revert_array[0]:
        result[index] = revert_array[len(revert_array) - 1]
print(f'Заменили значения и получили результат: {result}')
















