"""

Задача №9.
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

"""

print('Введите последовательно натуральные числа. После ввода каждого числа, нажмите "Enter". Для завершения ввода чисел, введите 0.')
usernumber = int(input('Введите число: '))
max_summary = 0
max_number = 0


while usernumber != 0:
    maxim = usernumber
    summary = 0
    while usernumber > 0:
        summary += usernumber % 10
        usernumber //= 10
    if summary > max_summary:
        max_summary = summary
        max_number = maxim
    usernumber = int(input('Введите число: '))
print(f'Наибольшее число по сумме цифр {max_number}, сумма цифр: {max_summary}.')






