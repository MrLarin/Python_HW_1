# Удаление абв через lambda c использование filter
str = 'Привет абв Влад, я люблю любабвлю мир'


def delet(str):
    str = list(filter(lambda i: 'абв' not in i, str.split()))
    return ' '.join(str)


str = delet(str)
print(str)

# Вывод максимального через map
num = print(max(list(map(int, input().split(',')))))
print(num)


# Вывод на экран i в степени j через enumerate
list_1 = [2, 3, 4, 5, 6]
list_2 = [print(i, '**', j, '=', i**j) for i, j in enumerate(list_1) if i > 0]


# вывести четные элементы
data = (list(map(int, input().split(','))))
print(data)
res = list(filter(lambda x: not x % 2, data))
print(res)
