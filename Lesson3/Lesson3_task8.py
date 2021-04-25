"""

Задача №8.
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

"""

matrix_neo = []

for i in range(4):
    start = 0
    sum = 0
    int_row = [int(number) for number in (input(f'Введите 4 числа {i+1} строки матрицы через запятую: ')).split(',')]
    while start <= len(int_row):
        try:
            sum += int_row[start]
            start += 1
        except IndexError:
            break
    int_row.append(sum)
    matrix_neo.append(int_row)

for a in matrix_neo:
    print(('{:>4d}' * 5).format(*a))

















