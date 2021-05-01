"""

Задача №2.
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

"""


print("Посчитаем четные и нечетные цифры введенного натурального числа.")
natur = int(input('Введите натуральное число: '))

even = odd = 0
def countnatur(even, odd, natur):
    if natur > 0:
        if natur % 2 == 0:
            even += 1
        else:
            odd += 1
        natur = natur // 10
    else:
        result = f'Четных цифр - {even}. Нечетных цифр - {odd}'
        print(result)
        return result
    countnatur(even, odd, natur)

countnatur(even, odd, natur)





