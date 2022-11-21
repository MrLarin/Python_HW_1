# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Удаление через replace(удаляет только то, что указал)
from random import randint
st = 'Привет Влад, абв как делаабв?'
print("Исходная строка: " + st)
res_st = st.replace('абв', '')
print("Строка после удаления всех символов абв: " + res_st)

# # Удаление через for (удаляет полностью все слово содержащее указ. символы)
st = 'Привет Влад, абв как делаабв?'
print("Исходная строка: " + st)
find_txt = "абв"
list = [i for i in st.split() if find_txt not in i]
print(f'Результат: {" ".join(list)}')


# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""


def input_int(msg=""):
    while True:
        try:
            result = int(input(msg))
        except ValueError:
            print("Ошибка, повторите ввод")
        else:
            return result


def start_multiplayer_game(initial_amount=2021, max_move=28):
    print(
        f"Начало игры, на столе лежит {initial_amount} конфет, вы можете взять от 1 до {max_move} конфет.")
    is_first_player_move = True
    current_player = "Первый"
    amount = initial_amount
    while amount > 0:
        while True:
            current_player = "Первый" if is_first_player_move else "Второй"
            move = input_int(
                f"{current_player} игрок, ваш ход. На столе осталось {amount} конфет, введите количество конфет: ")
            if 1 <= move <= max_move and move <= amount:
                break
            else:
                print("Вы не можете взять столько конфет")
        amount -= move
        is_first_player_move = not is_first_player_move
    print(
        f"Поздравляем Вас, {current_player} игрок. Вы взяли последние конфеты и победили.")


def start_random_bot_game(initial_amount=2021, max_move=28):
    print(
        f"Начало игры, на столе лежит {initial_amount} конфет, вы можете взять от 1 до {max_move} конфет.")
    is_human_player_move = bool(randint(0, 1))
    amount = initial_amount
    while amount > 0:
        while True:
            if is_human_player_move:
                move = input_int(
                    f"Ваш ход. На столе осталось {amount} конфет, введите количество конфет: ")
            else:
                move = randint(1, max_move if amount > max_move else amount)
                print(
                    f"На столе оставалось {amount} конфет. Бот(случайный) сделал ход. Он взял {move} конфет")
            if 1 <= move <= max_move and move <= amount:
                break
            else:
                print("Вы не можете взять столько конфет")
        amount -= move
        is_human_player_move = not is_human_player_move
    if not is_human_player_move:
        print("Поздравляем Вас. Вы взяли последние конфеты и победили.")
    else:
        print("К сожалению, вы проиграли, Бот(случайный) взял последние конфеты и победил")


def startstrategic_bot_game(initial_amount=2021, max_move=28):
    print(
        f"Начало игры, на столе лежит {initial_amount} конфет, вы можете взять от 1 до {max_move} конфет.")
    is_human_player_move = bool(randint(0, 1))
    amount = initial_amount
    while amount > 0:
        while True:
            if is_human_player_move:
                move = input_int(
                    f"Ваш ход. На столе осталось {amount} конфет, введите количество конфет: ")
            else:
                leftover = amount % max_move
                if leftover == 0:
                    move = randint(1, max_move if amount >
                                   max_move else amount)
                else:
                    move = leftover
                print(
                    f"На столе оставалось {amount} конфет. Бот(стратегический) сделал ход. Он взял {move} конфет")
            if 1 <= move <= max_move and move <= amount:
                break
            else:
                print("Вы не можете взять столько конфет")
        amount -= move
        is_human_player_move = not is_human_player_move
    if not is_human_player_move:
        print("Поздравляем Вас. Вы взяли последние конфеты и победили.")
    else:
        print("К сожалению, вы проиграли, Бот(стратегический) взял последние конфеты и победил")


print('Добро пожаловать в игру "Забери конфетку"')
while True:
    print("Выберите режим игры:")
    print("1 - Два игрока")
    print("2 - Против Бота(случайный)")
    print("3 - Против Бота(стратегический)")
    mode = input_int()
    if 1 <= mode <= 3:
        break
    print("Неправильный ввод")
amount = input_int("Введите общее количество конфет: ")
max_move = input_int(
    "Введите максимальное количество конфет, которое можно взять за один ход: ")

if mode == 1:
    start_multiplayer_game(amount, max_move)
elif mode == 2:
    start_random_bot_game(amount, max_move)
elif mode == 3:
    startstrategic_bot_game(amount, max_move)


# Создайте программу для игры в ""Крестики-нолики"".


empty_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def print_field(field):
    print("    0   1   2   ")
    print("  ┌───┬───┬───┐")
    print("0 │ "+" │ ".join(field[0])+" │")
    print("  ├───┼───┼───┤")
    print("1 │ "+" │ ".join(field[1])+" │")
    print("  ├───┼───┼───┤")
    print("2 │ "+" │ ".join(field[2])+" │")
    print("  └───┴───┴───┘")


def make_move(field, move, symbol):
    result = field.copy()
    move = move.split()
    [x, y] = list(map(int, move))
    if (3 > x >= 0) and (3 > y >= 0) and result[y][x] == " ":
        result[y][x] = symbol
    else:
        new_attempt = input("Неправильный ход, повторите ввод: ")
        result = make_move(field, new_attempt, symbol)
    return result


def check_win(field):
    # проверка ряда
    for row in field:
        if row[0] == "X" and row[1] == "X" and row[2] == "X":
            return "X"
        if row[0] == "0" and row[1] == "0" and row[2] == "0":
            return "0"
    # проверка колонки
    for col in range(3):
        if field[0][col] == "X" and field[1][col] == "X" and field[2][col] == "X":
            return "X"
        if field[0][col] == "0" and field[1][col] == "0" and field[2][col] == "0":
            return "0"
    # проверка диагонали
    if field[0][0] == "X" and field[1][1] == "X" and field[2][2] == "X":
        return "X"
    if field[0][2] == "X" and field[1][1] == "X" and field[2][0] == "X":
        return "X"
    if field[0][0] == "0" and field[1][1] == "0" and field[2][0] == "0":
        return "0"
    if field[0][2] == "0" and field[1][1] == "0" and field[2][0] == "0":
        return "0"
    return None


field = empty_field
moves_count = 0
is_X_move = True
print("Добро пожаловать в игру X-0. В свой ход вводите координаты, разделенные пробелом.")
print_field(field)
while check_win(field) == None and moves_count < 9:
    current_player = "X" if is_X_move else "0"
    field = make_move(field, input(
        f"Ход игрока {current_player}: "), current_player)
    print_field(field)
    is_X_move = not is_X_move
    moves_count += 1
print("Игра окончена")
result = check_win(field)
if result == None:
    print("Ничья")
else:
    print(f"Победитель: игрок {result}")

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def decompression(str):
    s = ""
    for i in range(1, len(str)+1, 2):
        for z in range(int(str[i])):
            s += str[i-1]
    return s


def compression(str):
    s = ""
    count = 1
    char = str[0]
    for i in range(1, len(str)):
        if str[i] == char and i != len(str)-1:
            count += 1
        else:
            s += char + f'{count}'
            count = 1
            char = str[i]
    return s


inputdata = open('file.txt', 'r')
outputdata = open('file_5.txt', 'w')
input = inputdata.read()
print(input)
str = compression(input)
outputdata.write(str)

output = open('file_5.txt', 'r')
findata = open('file_6.txt', 'w')
comp = output.read()
print(comp)
res = decompression(comp)
findata.write(res)
