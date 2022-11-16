# Функция фибоначчи

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Вызываем функцию фибоначчи


list = []
for i in range(1, 10):
    list.append(fib(i))
print(list)
