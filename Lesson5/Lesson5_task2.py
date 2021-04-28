"""

Задача №2. Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""
from collections import deque

first_number = deque(list(input('Введите первое шестнадцатеричное число: ')))
second_number = deque(list(input('Введите второе шестнадцатеричное число: ')))

a, b = first_number.copy(), second_number.copy()

# сумма
def sum_case(a, b):
    short_case = None
    if len(a) > len(b):
        for zero in range(len(a) - len(b)):
            a.appendleft('0')
    elif len(a) < len(b):
        for zero in range(len(b) - len(a)):
            a.appendleft('0')
    elif len(b) == len(a) == 1:
        short_case = '1'

    row_16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    dict_16 = {row_16[number]: number for number in range(16)}
    result = []
    addition = 0

    def get_key(value):
        for k, v in dict_16.items():
            if v == value:
                return k
    while b:
        value = dict_16[a.pop()] + dict_16[b.pop()] + addition
        addition = 0
        if value > 16:
            value -= 16
            addition += 1
        value = get_key(value)
        result.append(value)
        if short_case:
            result.append(short_case)
    result.reverse()

    print(f'Сумма чисел: {result}')

    return list(result)


def mult(x, y):
    dict_16 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    spam = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = dict_16[y.pop()]

        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * dict_16[x[j]])

        for _ in range(i):
            spam[i].append(0)

    addition = 0

    for _ in range(len(spam[-1])):
        res = addition

        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()

        if res < 16:
            result.appendleft(dict_16[res])

        else:
            result.appendleft(dict_16[res % 16])
            addition = res // 16

    if addition:
            result.appendleft(dict_16[addition])

    print(f'Произведение чисел: {list(result)}')

    return list(result)

sum_case(a, b)
mult(first_number, second_number)









