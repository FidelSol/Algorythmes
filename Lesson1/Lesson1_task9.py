"""

Задача №9.
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

"""
print('Введите три разных числа: ')
a = int(input('Первое число:'))
b = int(input('Второе число:'))
c = int(input('Третье число:'))

if b < a < c or c < a < b:
    print('Среднее число:', a)
elif a < b < c or c < b < a:
    print('Среднее число:', b)
else:
    print('Среднее число:', c)



