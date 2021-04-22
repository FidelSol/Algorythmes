"""

Задача №4.
Определить, какое число в массиве встречается чаще всего.

"""
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


# долго думал, как же не использовать функции count и аналогичные - в итоге пришел к словарю,
# который выводит количества всех повторяющихся больше одного раза числа
COUNTER = 0
indexresult = {}

for index in range(len(revert_array)):
    try:
        if revert_array[index] == revert_array[index + 1]:
            COUNTER += 1
        else:
            indexresult.update({revert_array[index]: COUNTER + 1})
            COUNTER = 0
    except IndexError:
        break
print(indexresult)

# и обычный вариант
num = revert_array[0]
max_meet = 1
for i in range(len(revert_array) - 1):
    meet = 1
    for k in range(i+1, len(revert_array)):
        if revert_array[i] == revert_array[k]:
            meet += 1
    if meet > max_meet:
        max_meet = meet
        num = revert_array[i]

print('Число ', num, ':', max_meet, 'раз.')


















