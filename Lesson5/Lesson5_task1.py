"""

Задача №1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

"""
from collections import namedtuple

concerns = []
Concern = namedtuple('Concern', ['name', 'profit_year'])

for number, unit in enumerate(range(int(input('Введите количество предприятий: ')))):
    concerns.append(Concern(name=input(f'Введите название {number + 1}-го предприятия: '),
                            profit_year=sum([int(input(f'Введите прибыль за {quarter + 1} квартал: ')) for quarter in range(4)])))

average_profit = sum([concerns[number].profit_year for number in range(len(concerns))]) / len(concerns)
lower_profit = tuple(concerns[number].name for number in range(len(concerns)) if concerns[number].profit_year < average_profit)
higher_profit = tuple(concerns[number].name for number in range(len(concerns)) if concerns[number].profit_year > average_profit)

print(f'Средняя прибыль для всех предприятий за год - {average_profit}.\nПредприятия, чья прибыль ниже средней за год - {lower_profit}.\nПредприятия, чья прибыль выше средней за год - {higher_profit}.')









