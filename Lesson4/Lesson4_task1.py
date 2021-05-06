"""

Задача №1.
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках
домашнего задания первых трех уроков.

"""

# Урок №2 Задача №3: В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import cProfile
import random
import timeit

# Функция генерации списков:
def generate_array(n):
    array = [random.randint(-201, 201) for i in range(n)]
    return array

step1 = generate_array(100)
step2 = generate_array(500)
step3 = generate_array(1000)
step4 = generate_array(2000)
step5 = generate_array(5000)
step6 = generate_array(10000)
step7 = generate_array(15000)
step8 = generate_array(20000)
step9 = generate_array(30000)
step10 = generate_array(50000)


# Вариант №1. Плохое решение:
def my_bad_solution(first_array):
    result = list.copy(first_array)
    revert_array = []
    while first_array != []:
        for index in range(len(first_array) - 1):
            if first_array[index] > first_array[index + 1]:
                first_array[index], first_array[index + 1] = first_array[index + 1], first_array[index]
        if first_array != []:
            revert_array.extend([first_array.pop(len(first_array) - 1)])

    for index in range(len(result)):
        if result[index] == revert_array[len(revert_array) - 1]:
            result[index] = revert_array[0]
        elif result[index] == revert_array[0]:
            result[index] = revert_array[len(revert_array) - 1]

    return result

print(timeit.timeit('my_bad_solution(step1)', number=100, globals=globals())) # 0.0007129999999999914
print(timeit.timeit('my_bad_solution(step2)', number=100, globals=globals())) # 0.016340300000000002
print(timeit.timeit('my_bad_solution(step3)', number=100, globals=globals())) # 0.06993210000000002
print(timeit.timeit('my_bad_solution(step4)', number=100, globals=globals())) # 0.2858366
print(timeit.timeit('my_bad_solution(step5)', number=100, globals=globals())) # 1.8407706999999998
print(timeit.timeit('my_bad_solution(step6)', number=100, globals=globals())) # 7.0612242
print(timeit.timeit('my_bad_solution(step7)', number=100, globals=globals())) # 16.5100526
print(timeit.timeit('my_bad_solution(step8)', number=100, globals=globals())) # 30.2133166
print(timeit.timeit('my_bad_solution(step9)', number=100, globals=globals())) # 66.76122480000001
print(timeit.timeit('my_bad_solution(step10)', number=100, globals=globals())) # 181.1419216

cProfile.run('my_bad_solution(step7)') # step7 -> n = 15000

"""

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000   16.614   16.614  <string>:1(<module>)
    1   16.598   16.598   16.613   16.613  Lesson4_task1.py:32(my_bad_solution)
    1    0.000    0.000   16.614   16.614  {built-in method builtins.exec}
45042    0.008    0.000    0.008    0.000  {built-in method builtins.len}
    1    0.000    0.000    0.000    0.000  {method 'copy' of 'list' objects}
    1    0.000    0.000    0.000    0.000  {method 'disable' of '_lsprof.Profiler' objects}
15000    0.002    0.000    0.002    0.000  {method 'extend' of 'list' objects}
15000    0.004    0.000    0.004    0.000  {method 'pop' of 'list' objects}


"""

# Вариант №2. Второе решение:
def second_variant(first_array):
    idx_min = 0
    idx_max = 0
    for i in range(len(first_array)):
        if first_array[i] < first_array[idx_min]:
            idx_min = i
        elif first_array[i] > first_array[idx_max]:
            idx_max = i
    first_array[idx_min], first_array[idx_max] = first_array[idx_max], first_array[idx_min]

    return first_array


print(timeit.timeit('second_variant(step1)', number=100, globals=globals())) # 0.0009670999999999985
print(timeit.timeit('second_variant(step2)', number=100, globals=globals())) # 0.004988799999999988
print(timeit.timeit('second_variant(step3)', number=100, globals=globals())) # 0.010134399999999988
print(timeit.timeit('second_variant(step4)', number=100, globals=globals())) # 0.020444500000000004
print(timeit.timeit('second_variant(step5)', number=100, globals=globals())) # 0.052524299999999996
print(timeit.timeit('second_variant(step6)', number=100, globals=globals())) # 0.10086020000000001
print(timeit.timeit('second_variant(step7)', number=100, globals=globals())) # 0.14299119999999998
print(timeit.timeit('second_variant(step8)', number=100, globals=globals())) # 0.2008107
print(timeit.timeit('second_variant(step9)', number=100, globals=globals())) # 0.3143153999999999
print(timeit.timeit('second_variant(step10)', number=100, globals=globals())) # 0.48188759999999986


cProfile.run('second_variant(step10)') # step7 -> n = 15000

"""

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1    0.000    0.000    0.005    0.005 <string>:1(<module>)
1    0.005    0.005    0.005    0.005 Lesson4_task1.py:79(second_variant)
1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""

# Вариант №3. Третье решение:
def third_variant(first_array):
    max = first_array[0]
    min = first_array[0]

    for i in first_array:
        if i > max:
            max = i
        elif i < min:
            min = i
    min_index = first_array.index(min)
    max_index = first_array.index(max)
    first_array[min_index], first_array[max_index] = first_array[max_index], first_array[min_index]

    return first_array

print(timeit.timeit('third_variant(step1)', number=100, globals=globals())) # 0.0005499999999999949
print(timeit.timeit('third_variant(step2)', number=100, globals=globals())) # 0.003014899999999987
print(timeit.timeit('third_variant(step3)', number=100, globals=globals())) # 0.004394700000000001
print(timeit.timeit('third_variant(step4)', number=100, globals=globals())) # 0.008859300000000014
print(timeit.timeit('third_variant(step5)', number=100, globals=globals())) # 0.023214999999999986
print(timeit.timeit('third_variant(step6)', number=100, globals=globals())) # 0.04162759999999999
print(timeit.timeit('third_variant(step7)', number=100, globals=globals())) # 0.06164709999999998
print(timeit.timeit('third_variant(step8)', number=100, globals=globals())) # 0.0847462
print(timeit.timeit('third_variant(step9)', number=100, globals=globals())) # 0.12137800000000004
print(timeit.timeit('third_variant(step10)', number=100, globals=globals())) # 0.21941520000000003


cProfile.run('third_variant(step10)') # step7 -> n = 15000

"""

 ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.001    0.001 <string>:1(<module>)
    1    0.002    0.002    0.002    0.002 Lesson4_task1.py:120(third_variant)
    1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


"""


"""
Вывод: 
График находится в файле chart.js.

Как мы видим на графике chart.html - Все три  алгоритма имеют линейную сложность O(n), но первый алгоритм стремится 
к квадратичной сложности O(n**2), что обусловлено двумя вложенными циклами и большим количеством операций внутри алгоритма.

1 вариант решения - очевидно самый худший. Мы видим, что время увеличивается намного больше при увеличении данных, 
если сравнить с остальными алгоритмами. cProfile нам позволяет увидеть, что алгоритм делает 45.000 вызовов функции len,
15.000 вызовов функции вставок и удаления элементов из массивов, при выборке данных 15.000 - алгоритм необходимо оптимизтировать.
Он эффективен примерно как остальные алгоритмы только при выборке данных до 500.

2 вариант решения - по сравнению с первым вариантом превосходен и прост, количество операций минимально.

3 вариант решения - по времени самый быстрый, хоть и количество количество операций (index) больше на единицу.


"""









