"""

Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.


Урок №5 - Задача №1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.



Python 3.9.0;
OS - 64 bit;
"""

# функция расчета памяти + для классов
import sys
from numbers import Number
from collections import namedtuple, Set, deque, Mapping, defaultdict

zero_depth_bases = (str, bytes, Number, range, bytearray)
items = 'items'

# во имя мазохизма - хочу посчитать память и классов
def getsize(obj_0):
    """Рекурсивный итератор для объектов и объектов по их ссылкам."""
    _seen_ids = set()
    def inner(obj):
        obj_id = id(obj)
        if obj_id in _seen_ids:
            return 0
        _seen_ids.add(obj_id)
        size = sys.getsizeof(obj)
        if isinstance(obj, zero_depth_bases):
            pass
        elif isinstance(obj, (tuple, list, Set, deque)):
            size += sum(inner(i) for i in obj)
        elif isinstance(obj, Mapping) or hasattr(obj, items):
            size += sum(inner(k) + inner(v) for k, v in getattr(obj, items)())
        # Проверяем свои объекты
        if hasattr(obj, '__dict__'):
            size += inner(vars(obj))
        if hasattr(obj, '__slots__'): # __slots__ вместе с __dict__
            size += sum(inner(getattr(obj, s)) for s in obj.__slots__ if hasattr(obj, s))
        return size
    return inner(obj_0)

# пусть количество предприятий будет задано заранее как и остальные данные
count_units = 3
names = ['ООО "Рога"', 'ОАО "Копыта"', 'ПАО "Хвост"']
profit_quarters = [[10, 20, 30, 40], [22, 34, 34, 66], [21, 23, 23, 59]]

# 1 вариант через список и именованный кортеж
concerns = []
Concern = namedtuple('Concern', ['name', 'profit_year'])

for number, unit in enumerate(range(count_units)):
    concerns.append(Concern(name=names[number], profit_year=sum(profit_quarters[number])))

average_profit = sum([concerns[number].profit_year for number in range(len(concerns))]) / len(concerns)
lower_profit = tuple(concerns[number].name for number in range(len(concerns)) if concerns[number].profit_year < average_profit)
higher_profit = tuple(concerns[number].name for number in range(len(concerns)) if concerns[number].profit_year > average_profit)

print(f'Средняя прибыль для всех предприятий за год - {average_profit}.\nПредприятия, чья прибыль ниже средней за год - {lower_profit}.\nПредприятия, чья прибыль выше средней за год - {higher_profit}.')

sum_size = getsize(count_units) + getsize(names) + getsize(profit_quarters) + getsize(range(count_units)) + getsize(concerns) + getsize(average_profit) + getsize(lower_profit) + getsize(higher_profit)
print(sum_size)

"""
На лекции Вы сказали, что в итераторах считать только последний - но я решил посчитать все, ведь элементов не много совсем.
Результат: задействовано 2248 байт.

"""

# 2 вариант через словарь и очередь
concerns = defaultdict()
prof_c = deque()
unprof_c = deque()
all_profit = 0
QUARTER = 4

for i in range(count_units):
    name = names[i]
    profit = 0
    concerns[name] = sum(profit_quarters[i])
    all_profit += sum(profit_quarters[i])

mid_profit = all_profit / count_units
for i, item in concerns.items():
    if item >= mid_profit:
        prof_c.append(i)
    else:
        unprof_c.append(i)
print(f'Средняя прибыль для всех компаний составила: {mid_profit}')
print(f'Прибыль выше среднего у {len(prof_c)} компаний:')
for name in prof_c:
    print(name)
print(f'Прибыль ниже среднего у {len(unprof_c)} компаний:')
for name in unprof_c:
    print(name)


sum_size = getsize(count_units) + getsize(names) + getsize(profit_quarters) + getsize(range(count_units))  + getsize(concerns) + getsize(all_profit) + getsize(prof_c) + getsize(unprof_c) + getsize(QUARTER)
print(sum_size)

"""

Результат: задействовано 3408 байт.

"""

# через список и класс
concerns = []

class Concern:
    def __init__(self, name, profit_year):
        self.name = name
        self.profit_year = profit_year

for number, unit in enumerate(range(count_units)):
    concerns.append(Concern(name=names[number], profit_year=sum(profit_quarters[number])))

average_profit = sum([concerns[number].profit_year for number in range(len(concerns))]) / len(concerns)
lower_profit = tuple(concerns[number].name for number in range(len(concerns)) if concerns[number].profit_year < average_profit)
higher_profit = tuple(concerns[number].name for number in range(len(concerns)) if concerns[number].profit_year > average_profit)

print(f'Средняя прибыль для всех предприятий за год - {average_profit}.\nПредприятия, чья прибыль ниже средней за год - {lower_profit}.\nПредприятия, чья прибыль выше средней за год - {higher_profit}.')

sum_size = getsize(count_units) + getsize(names) + getsize(profit_quarters) + getsize(range(count_units)) + getsize(concerns) + getsize(average_profit) + getsize(lower_profit) + getsize(higher_profit)
print(sum_size)

"""

Результат: задействовано 2649 байт.

Вывод: Вариант с использованием класса оказался самым эффективным в плане затрат, используя функцию с учетом ссылок и метода __dict__.
Использование очередей и словаря более затратны. 

"""