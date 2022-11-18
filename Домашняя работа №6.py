import random
# Задача 1. Создайте программу для игры в "Крестики-нолики".
field = []
def print_field (field_print):
    for i in range (3):
        print("  ".join(field_print[i]))

for i in range (3):
    fieldrow = []
    for j in range (3):
        fieldrow.append ('-')
    field.append (fieldrow)
print_field(field)

def player_move (field_print):
    try:
        move = input('Введите координаты через запятую от 0 до 2 ')
        move_coord = move.split(',')
        x = int(move_coord[0])
        y = int(move_coord[1])
        if field[x][y] == 'X' or field[x][y] == 'O':
            print('Пропускаете свой ход по причине ввода некорректных данных')
            return field_print
        else:
            field [x][y] = 'X'
            return field_print
    except:
        print('Пропускаете свой ход по причине ввода некорректных данных')
        return field_print

def comp_move (field_print):
    print('ходит бот')
    x = random.randint(0,2)
    y = random.randint(0,2)
    while field [x][y] != '-':
        x = random.randint(0,2)
        y = random.randint(0,2)
    field[x][y] = 'O'
    return field_print

def who_win(a):
    if field[0][0]==field[0][1]==field[0][2]==a or field[1][0]==field[1][1]==field[1][2]==a  or field[2][0]==field[2][1]==field[2][2]==a :
        if a == 'X':
            print('Вы выйграли')
            a = True
        else:
            print('Бот выйграл')
            a = True
    elif field[0][0]==field[1][0]==field[2][0]==a or field[0][1]==field[1][1]==field[2][1]==a  or field[0][2]==field[1][2]==field[2][2]==a :
        if a == 'X':
            print('Вы выйграли')
            a = True
        else:
            print('Бот выйграл')
            a = True
    elif field[0][0]==field[1][1]==field[2][2]==a or field[0][2]==field[1][1]==field[2][0]==a:
        if a == 'X':
            print('Вы выйграли')
            a = True
        else:
            print('Бот выйграл')
            a = True
    return a

for m in range (10):
    if m == 9:
        print('Ничья')
        break
    elif m%2 == 0: 
        field = player_move(field)
        print_field(field)
        if who_win('X') == True:
            break
    else:
        field = comp_move(field)
        print_field(field)
        if who_win('O') == True:
            break

# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

text = "13 * 3 - 2 * 3 + 3 - 8 / 2"
result = text.split(' ')
temp_result = None
x = 1
length = len(result)
while x < length:
      for i in range (len(result)):
        if result[i] == '*':
            temp_result = int(result[i-1]) * int(result[i+1])
            result[i] = temp_result
            del result[i-1]
            del result[i]
            x += 1
            break
        else:
            x +=1
x = 1
while x < length:
      for i in range (len(result)):
        if result[i] == '/':
            temp_result = int(result[i-1]) / int(result[i+1])
            result[i] = temp_result
            del result[i-1]
            del result[i]
            x += 1
            break
        else:
            x +=1
x = 1
while x < length:
      for i in range (len(result)):
        if result[i] == '-':
            temp_result = int(result[i-1]) - int(result[i+1])
            result[i] = temp_result
            del result[i-1]
            del result[i]
            x += 1
            break
        elif result[i] == '+':
            temp_result = int(result[i-1]) + int(result[i+1])
            result[i] = temp_result
            del result[i-1]
            del result[i]
            x += 1
            break
        else:
            x +=1
print(text, '=', result[0])