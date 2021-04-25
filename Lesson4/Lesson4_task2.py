"""

Задача №2.
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»


"""

# Решето Эратосфена
import cProfile
import math
import timeit


def resheto(n):
    number_of_primes = 0
    number = 2
    while number_of_primes <= n:
        number_of_primes = number / math.log(number)
        number += 1

    s = [x for x in range(2, number+1) if x not in [i for sub in [list(range(2 * j, number+1, j)) for j in range(2, number // 2)] for i in sub]]
    return s[n-1]

print(timeit.timeit('resheto(5)', number=100, globals=globals())) # 0.004826800000000003
print(timeit.timeit('resheto(10)', number=100, globals=globals())) # 0.031514099999999996
print(timeit.timeit('resheto(20)', number=100, globals=globals())) # 0.19487819999999997
print(timeit.timeit('resheto(30)', number=100, globals=globals())) # 0.5747092
print(timeit.timeit('resheto(40)', number=100, globals=globals())) # 1.2731383000000003
print(timeit.timeit('resheto(50)', number=100, globals=globals())) # 2.285884
print(timeit.timeit('resheto(60)', number=100, globals=globals())) # 3.8521494
print(timeit.timeit('resheto(70)', number=100, globals=globals())) # 6.0543952
print(timeit.timeit('resheto(80)', number=100, globals=globals())) # 8.435184000000001
print(timeit.timeit('resheto(90)', number=100, globals=globals())) # 11.5518766


cProfile.run('resheto(90)') # n = 90

"""

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.119    0.119 <string>:1(<module>)
    1    0.000    0.000    0.119    0.119 Lesson4_task2.py:17(resheto)
    1    0.012    0.012    0.118    0.118 Lesson4_task2.py:24(<listcomp>)
    1    0.000    0.000    0.119    0.119 {built-in method builtins.exec}
  571    0.000    0.000    0.000    0.000 {built-in method math.log}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

# Без решета
def without_resheto(n):
    prime_array = [2]
    number = 3
    while len(prime_array) < n:
        flag = True
        for j in prime_array.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            prime_array.append(number)
        number += 1
    return prime_array[-1]

print(timeit.timeit('without_resheto(5)', number=100, globals=globals())) # 0.00028579999999999925
print(timeit.timeit('without_resheto(10)', number=100, globals=globals())) # 0.0009223000000000009
print(timeit.timeit('without_resheto(20)', number=100, globals=globals())) # 0.002556599999999999
print(timeit.timeit('without_resheto(30)', number=100, globals=globals())) # 0.004770300000000002
print(timeit.timeit('without_resheto(40)', number=100, globals=globals())) # 0.007899800000000005
print(timeit.timeit('without_resheto(50)', number=100, globals=globals())) # 0.0114357
print(timeit.timeit('without_resheto(60)', number=100, globals=globals())) # 0.015423
print(timeit.timeit('without_resheto(70)', number=100, globals=globals())) # 0.021200800000000006
print(timeit.timeit('without_resheto(80)', number=100, globals=globals())) # 0.025369199999999995
print(timeit.timeit('without_resheto(90)', number=100, globals=globals())) # 0.031491799999999986

cProfile.run('without_resheto(90)') # n = 90

"""

 ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.001    0.001 <string>:1(<module>)
    1    0.001    0.001    0.001    0.001 Lesson4_task2.py:54(without_resheto)
    1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
  462    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   89    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
  461    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  

"""


"""

Вывод: Как видно из графика chart.html - оба алгоритма имеют линейную O(n) сложность, второй алгоритм намного быстрее первого.
Хоть в первом алгоритме и меньше операций, но генератор списков требует намного больше времени 
для определения простого числа. 
Второй алгоритм (без решета Эратосфена) - более эффективный, но имеет больше операций. 



"""