# # Функция фибоначчи

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# # Вызываем функцию фибоначчи

# list = []
# for i in range(1, 10):
#     list.append(fib(i))
# print(list)

# функция удаления букв в строке

# def deleteName(str, delStr):
#     with open('file_2.txt', 'w') as data:
#         data.write(str.replace(f'{delStr}', ''))
#         data.close
#     return (str.replace(f'{delStr}', ''))

#                      ДОПОЛНИТЕЛЬНЫЙ СЕМИНАР №1

# Квадрат числа

#  функция

# def sqr(n):
#     n = n ** 2
#     return (n)

# n = int(input())
# print(sqr(n))

# в одну строчку
# print(int(input()) ** 2)

# Вход два числа. Является ли одно квадратом другого
# через оператор or

# a = int(input())
# b = int(input())
# if (a ** 2 == b or b ** 2 == a):
#     print('Являетс)я')
# else:
#     print("Не Являтся")

# через оператор if - elif - else

# a, b = int(input()), int(input())
# if a ** 2 == b:
#     print('Являетс)я')
# elif b ** 2 == a:
#     print('Являетс)я')
# else:
#     print("Не Являтся")

# решим чере список
# split() - разбивает строку на списки по каким-то символам. Указывваем в скобках.
# в данном случае по пробелам
#  Вводим: 2 3 4 5 6 7 8
# Получаем: ['2', '3', '4', '5', '6', '7', '8']

# c = input().split()  # записывает символы в список(массив) как строки
# a = int(c[0])   # int - переводит в число строку
# b = int(c[1])
# if (a ** 2 == b or b ** 2 == a):
#     print('Являетс)я')
# else:
#     print("Не Являтся")

# Вход 5 чисел. Вывод аксимального.

# ввод через список
# числа вводимые с клав. разделяются Splitom(,) через запятую, записываются в список и функция "map"  сразу ко всем применяеи int.
# split разделяет строку по тому что в скобках и записывает аргумент в список
# map применяет к каждому элементу списка указан. ф-ию(int)
# list - перевод в массив

# num = print(max(list(map(int, input().split(',')))))  # в одну строчку
# print(max(num))

# ввод через цикл for
# max = int(input())
# for i in range(5):  # цикл от 1 до 5
#     a = int(input())
#     if a > max:
#         max = a
# print(max)

# Вход число N. Вывод -N:N

# через while
# n = int(input())
# i = -n
# while i <= n:
#     print(i)
#     i += 1

# через for
# n = int(input())
# mas = []  # создали массив пустой
# for i in range(-n, n+1, 1):  # идем от  одного значения к другому с шагом 1
#     mas.append(i)  # добавили в массив элементы - т.е. - i
# print(mas)

# или такой вывод с end
# n = int(input())
# for i in range(-n, n+1, 1):  # идем от  одного значения к другому с шагом 1
#     # end - выводит все значения i. в (указываешь разделитель при выводе)
#     print(i, end=',')
#     # 3
#     # -3,-2,-1,0,1,2,3,

# На входе дробь. Вывод - первая цифра дробной части

# через математику
# n = float(input())
# # число 2,33*10=23,3 -> int(23,3)=23 -> 23%10 Это 23/10 = 2,3 Ост=3
# a = int(n*10) % 10
# print(a)

# через строку
# -> если ввели целое число 3->через float в 3.0-> через str в строку 3.0
# n = str(float(input()))
# # find (n.find('.')) - возвращает индекс искомого значения. 2.33 -> индекс -> 1
# print(n[n.find('.')+1])

# на вход число! Прверить кратно ли оно 5 и (10 или 15),но не 30

# n = int(input())
# if (n % 5 == 0 and (n % 10 == 0 or n % 15 == 0)) and n % 30 != 0:
#     print('Кратное')
# else:
#     print('Не Кратное')

# * в функции Print
# my_list = [213, 'sdf', True, 34.23]
# print(my_list)
# print(*my_list)
# print('\nНовый принт')
# print()
# print(*my_list, sep='\n', end='\n')  # sep - разделитель, end - что в конце


#                      ДОПОЛНИТЕЛЬНЫЙ СЕМИНАР №2
