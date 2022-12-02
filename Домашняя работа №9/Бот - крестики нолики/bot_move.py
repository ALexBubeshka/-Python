import random
import field


def comp_move (field_print):
    global field
    print('ходит бот')
    x = random.randint(0,2)
    y = random.randint(0,2)
    while field.field [x][y] != '-':
        x = random.randint(0,2)
        y = random.randint(0,2)
    field.field[x][y] = 'O'
    return field_print