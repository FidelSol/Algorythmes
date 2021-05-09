"""

Задача №1.  Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.

"""
from hashlib import sha1

st = input("Введите не пустую строку: ")

def count_understrings(string):
    length = len(string)

    is_counted = [string]
    under_strings = {}

    for i in range(length):
        for w in range(i + 1, length + 1):
            unders = string[i:w]
            if unders not in is_counted and unders not in under_strings:
                under_strings[unders] = 0

    for j in under_strings:
        j_length = len(j)
        j_hash = sha1(j.encode("utf-8")).hexdigest()
        for i in range(length - j_length + 1):
            subs_hash = sha1(string[i:i + j_length].encode("utf-8")).hexdigest()
            if subs_hash == j_hash:
                under_strings[j] += 1

    return under_strings

result = count_understrings(st)
result = sum(x for x in result.values())
print(f"Количество подстрок в строке - {result}")
