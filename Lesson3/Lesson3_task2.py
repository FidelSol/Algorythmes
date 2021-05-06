"""

Задача №2.
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.

"""
import random

first_array = [random.randint(0, 101) for i in range(15)]
print(first_array)

# стандартный на мой взгляд метод
result_array = [index for index, number in enumerate(first_array) if number % 2 == 0]
print(result_array)

# второй вариант - считать ли за костыль?
result_array = []
count = 0
for number in first_array:
    if number % 2 == 0:
        result_array.append(count)
    count += 1
print(result_array)














