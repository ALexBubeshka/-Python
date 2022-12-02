import field

def who_win(a):
    if field.field[0][0]==field.field[0][1]==field.field[0][2]==a or field.field[1][0]==field.field[1][1]==field.field[1][2]==a  or field.field[2][0]==field.field[2][1]==field.field[2][2]==a :
        if a == 'X':
            print('Вы выйграли')
            a = True
        else:
            print('Бот выйграл')
            a = True
    elif field.field[0][0]==field.field[1][0]==field.field[2][0]==a or field.field[0][1]==field.field[1][1]==field.field[2][1]==a  or field.field[0][2]==field.field[1][2]==field.field[2][2]==a :
        if a == 'X':
            print('Вы выйграли')
            a = True
        else:
            print('Бот выйграл')
            a = True
    elif field.field[0][0]==field.field[1][1]==field.field[2][2]==a or field.field[0][2]==field.field[1][1]==field.field[2][0]==a:
        if a == 'X':
            print('Вы выйграли')
            a = True
        else:
            print('Бот выйграл')
            a = True
    return a