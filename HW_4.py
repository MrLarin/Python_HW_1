# Вычислить число c заданной точностью d
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import random
d = int(input("Введите число точности числа Пи:\n"))
s = 0
sgn = 1
k = 201
while (s < 3.1415926535):
    s = 3
    for i in range(2, k, 2):
        s += ((sgn*4)/(i*(i+1)*(i+2)))
        sgn = -sgn
    k += 2
print(f"Число Пи с заданной точностью {d} равно {round(s, d)}")

# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

n = int(input())
a = [int(i) for i in range(1, n+1)]
simfactor = []
print(a)
for item in a:
    if not n % item:
        simfactor.append(item)
print(simfactor)

# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

# ввод последовательности чисел с клавиатуры через пробел. Преоб. в инт и запись в лист

numbers = [int(i) for i in input().split()]
list_uniq_num = []  # создал пустой список для добавления уникал.значений
# передал в множество список намберс. Он состоит только из уникальных значений
uniq_num = set(numbers)
for item in uniq_num:  # через иттератор добавил значения из множества в список!
    # добавляем в конец ссписка каждый элемент мнжества
    list_uniq_num.append(item)
print(list_uniq_num)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


def rand(k):
    r = []
    for i in range(k + 1):
        i = random.randint(0, 101)
        r.append(i)
    return r


def assembling(r):  # заполняем строку многочленами
    st = ''
    for i in range(len(r)-1, -1, -1):
        if r[i] > 1:
            if i == 0:
                st += str(r[i]) + ' + '
            elif i == 1:
                st += str(r[i]) + 'x' + ' + '
            else:
                st += str(r[i]) + 'x^' + str(i) + ' + '
        elif r[i] == 1:
            if i == 0:
                st += ' + '
            elif i == 1:
                st += 'x' + ' + '
            else:
                st += 'x^' + str(i) + ' + '
    st = st[:-3]
    st += ' = 0'
    return st


k = int(input("Введите натуральную степень: "))
r = rand(k)
print(f'{r} - Сформированый случайным образом список коэффициентов')
a = assembling(r)
print(f'{a} - записаный в файл многочлен в степени {k}')
data = 'file3.txt'
with open(data, 'w') as f_1:
    f_1.write(a)


# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# # Создал два файла, и записал в них многочлен
with open('file.txt', 'w') as data:
    data.write('2*x^2 + 3*x + 3')
with open('file2.txt', 'w') as data:
    data.write('3*x^2 + 2*x + 5')
# Открыл файл, прочитал и записал многочлен в переменную в ввиде строки
path = 'file.txt'
data = open(path, 'r')
s1 = ' '
for line in data:
    s1 += line
data.close()

path = 'file2.txt'
data = open(path, 'r')
s2 = ' '
for line in data:
    s2 += line
data.close()

print(f"Многочлен 1: {s1}")
print(f"Многочлен 2: {s2}")


def pure_polynomials(a):       # Отделение коэффициентов
    a = a[:-3]
    a = a.replace(' ', '').replace('^', '').split('+')
    c = ''
    b = []
    for i in range(len(a)):
        c = ''
        for j in a[i]:
            if j != 'x':
                c += str(j)
            else:
                break
        c = int(c)
        b.append(c)
    return b


pps1 = pure_polynomials(s1)
pps2 = pure_polynomials(s2)


def summ(f1, f2):   # суммируем коэф. многочлена
    sum = []
    for i in range(len(f1)):
        sum.append(f1[i] + f2[i])
    return sum


def assembling(r):  # заполняем строку многочленами
    st = ''
    for i in range(len(r)-1, -1, -1):
        if r[i] > 1:
            if i == 0:
                st += str(r[i]) + ' + '
            elif i == 1:
                st += str(r[i]) + 'x' + ' + '
            else:
                st += str(r[i]) + 'x^' + str(i) + ' + '
        elif r[i] == 1:
            if i == 0:
                st += ' + '
            elif i == 1:
                st += 'x' + ' + '
            else:
                st += 'x^' + str(i) + ' + '
    st = st[:-3]
    st += ' = 0'
    return st


print(f'{pps1} коэффициенты многочлена из 1-го файла')
print(f'{pps2} коэффициенты многочлена из 2-го файла')

s = summ(pps1, pps2)
print(f'{s} сумма коэф. многочленов\n')

assemb = assembling(s)
print(f'{assemb} Сформирован файл(4) содержащий сумму многочленов\n')

dpat = 'file4.txt'
with open(dpat, 'w') as f_3:
    f_3.write(assemb)
