"""

Задача №6.
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

"""
# как обычно - я отсортирую массив как в предыдущих задачах
# import random
#
# first_array = [random.randint(0, 101) for i in range(15)]
# result = list.copy(first_array)
#
# revert_array = []
# print(f'Сгенерировали список: {first_array}')
#
# while first_array != []:
#     for index in range(len(first_array) - 1):
#         if first_array[index] > first_array[index + 1]:
#             first_array[index], first_array[index + 1] = first_array[index + 1], first_array[index]
#     if first_array != []:
#         revert_array.extend([first_array.pop(len(first_array) - 1)])
# print(f'Отсортировали по убыванию: {revert_array}')

revert_array = [77, 75, 65, 63, 52, 47, 42, 41, 37, 37, 23, 23, 15, 14, 8]

revert_array.remove(revert_array[0])
sum_el = revert_array[0]


for index in range(len(revert_array)):
    try:
        sum_el += revert_array[index + 1]
    except IndexError:
        sum_el -= revert_array[index]
        break
print(f'Сумма: {sum_el}')



















