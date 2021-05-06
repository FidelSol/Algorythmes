"""

Задача №2.  Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

"""
import random

array = [round(random.uniform(0, 49.99), 2) for i in range(10)]
print(array)


def iter_merge(list1, list2):
    result, it1, it2 = [], iter(list1), iter(list2)
    el1 = next(it1, None)
    el2 = next(it2, None)
    while el1 is not None or el2 is not None:
        if el1 is None or (el2 is not None and el2 < el1):
            result.append(el2)
            el2 = next(it2, None)
        else:
            result.append(el1)
            el1 = next(it1, None)
    return result

def merge_sort(par):
    if len(par) <= 1:
        return par
    else:
        left = par[:len(par) // 2]
        right = par[len(par) // 2:]
    return iter_merge(merge_sort(left), merge_sort(right))

print(merge_sort(array))