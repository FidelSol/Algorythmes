"""

Задача №1.  Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

"""
import random

array = [random.randint(-100, 99) for i in range(10)]
print(array)

# с избавлением от ненужных шагов
def optimus_bubble(data):
    is_sorted = True
    while is_sorted:
        is_sorted = False
        for i in range(len(data) - 1):
            if data[i] < data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                is_sorted = True
    print(data)
    return data

optimus_bubble(array)