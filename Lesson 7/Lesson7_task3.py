"""

Задача №3.  Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы
, в другой — не больше медианы.


"""
import random

N = 10
array = [random.randint(0, 100) for _ in range(2 * N + 1)]
print(array)

def partition(L, v):
    smaller = []
    bigger = []
    for val in L:
        if val < v:
            smaller += [val]
        if val > v:
            bigger += [val]
    return (smaller, [v], bigger)

def top_k(L, k):
    if L != []:
        v = L[random.randrange(len(L))]
        (left, middle, right) = partition(L, v)
        if len(left) == k:
            return left
        if len(left)+1 == k:
            return left + middle
        if len(left) > k:
            return top_k(left, k)
        return left + middle + top_k(right, k - len(left) - len(middle))
    else:
        return []

def median(L):
    n = len(L)
    l = top_k(L, n / 2 + 1)
    return max(l)

print(median(array))