# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from decimal import Decimal
from math import ceil
list = [int(i) for i in input().split()]
print(list)
sum = 0
for i in range(len(list)):
    if i % 2 != 0:
        sum += list[i]
print(sum)

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [int(i) for i in input().split()]
print(list)
list2 = []
for i in range(ceil(len(list)/2)):
    list2.append(list[i] * list[-1-i])
print(list2)


# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [float(i) for i in input().split()]
print(list)
max = list[0] % 1
min = list[1] % 1
for i in range(len(list)):
    if (list[i] - int(list[i])) > max:
        max = list[i] - int(list[i])
    elif (list[i] - int(list[i])) < min:
        min = list[i] - int(list[i])
res = max-min
print(Decimal(res).quantize(Decimal('1.00')))


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число: '))
bi_num = []
while n > 0:
    bi_num.append(str(n % 2))  # добавление элементов в список
    n = n // 2
print(''.join(bi_num[::-1]))  # развернуть массив при выводе


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input('Введите число: '))
negafib = [1, 0, 1]
for i in range(n-1):
    thend = negafib[-1] + negafib[-2]
    thstart = (-1) ** (i + 1) * thend
    negafib.append(thend)
    negafib.insert(0, thstart)
print(*negafib)


# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
num = 8
my_list = [1, 0, 1]
for _ in range(1, num):
    print(my_list[0], my_list[1] - my_list[0])
    print(my_list[-1], my_list[-2] + my_list[-1])
    my_list.append(my_list[-2] + my_list[-1])
    my_list.insert(0, my_list[1] - my_list[0])
