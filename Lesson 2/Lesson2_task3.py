"""

Задача №3.
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.

"""


print("Сформируем обратное по порядку введенное число.")
num = int(input("Введите целое положительное число: "))
rank = 0

def revertnum(num, rank):
    if num > 0:
        rest = num % 10
        num = num // 10
        rank = rank * 10
        rank = rank + rest
    else:
        result = f'Обратное число - {rank}.'
        print(result)
        return result
    revertnum(num, rank)


revertnum(num, rank)





