# Удаление абв через lambda


str = 'Привет абв мир ,я любабвлю питонабв'


def delet(str):
    str = list(filter(lambda i: 'абв' not in i, str.split()))
    return ''.join(str)


str = delet(str)

print(str)
