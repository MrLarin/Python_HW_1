# Напишите программу,
# которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.
# Закоментировать все и сразу -> CTRL+/

# a = int(input())
# b = int(input())
# if a == b*b or b == a*a:
#     print('Yes')
# else:
#     print('NO')

# a = [int(i) for i in input().split(' ')]
# b = list(map(int, input().split()))
# a = [int(i) for i in input().split(' ')]  # list comprehension
# b = list(map(int, input().split()))  # обычный ввод списка с изменением
# names = input().split(',')  # ввод списка с клавиаутры БЕЗ ИЗМЕНЕНИЙ ЕГО ЭЛЕМЕНТОВ

# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# nums = [int(i) for i in input().split()]
# maxi = nums[0]
# for i in range(len(nums)):
#     if num > maxi:
#         maxi = num
# print(maxi)

# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# N = int(input())
# a = range(-N, N+1)
# for i in a:
#     print(i)

# Напишите программу,
# которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# n = float(input('Enter n: '))
# print(int((n - int(n))*10))


# Напишите программу,
# которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или (15, но не 30)
n = int(input('Enter n: '))
if (n % 5 == 0 and n % 10 == 0) or (n % 15 == 0 and not n % 30 == 0):
    print("YeS")
else:
    print('NO')
