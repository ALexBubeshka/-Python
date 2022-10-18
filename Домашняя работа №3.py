# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def creating_int_list(n, item):
    user_list = []
    n = int(input('Введите длину списка '))
    for i in range(0, n):
        item = int(input('Введите число '))
        user_list.append(item)
    print('Ваш cписок', user_list)
    return user_list

int_list = creating_int_list('Введите длину списка', 'Введите число ')

def sum_list(list):
    i = 0
    sum = 0
    while i < len(list):
        if i % 2 != 0:
            sum += list[i]
        i += 1
    return print('Сумму элементов списка, стоящих на нечётной позиции =', sum)

sum_list(int_list) 

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def multiplication_list(list):
    multi = []
    i = 0
    multiplication = 0
    z = -1
    a = 0
    if len(list) == 2:
            multiplication = list[0]*list[1]
            multi.append(multiplication)
    else:
        while i < len(list):
            multiplication = list[z]*list[a]
            i += 2
            z -= 1
            a += 1
            multi.append(multiplication)
    return print('Произведение пар чисел списка = ', multi)

multiplication_list(int_list)

# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def creating_float_list(n, item):
    user_list = []
    n = int(input('Введите длину списка '))
    for i in range(0, n):
        item = float(input('Введите вешественное число '))
        user_list.append(item)
    print('Ваш cписок', user_list)
    return user_list

float_list = creating_float_list('Введите длину списка', 'Введите вешественное число ')

def fiding_dif (list):
    i = 0
    max = list[0]%1
    min = list[0]%1
    for i in range(len(list)):
        if (list[i]%1) > max: 
            max=(list[i]%1)
        if (list[i]%1) < min:
             min=(list[i]%1)
    return print(max - min)

fiding_dif(float_list)

# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.

def finding_binar_number (n):
    n = int(input('Введите десятичное число '))
    number = n
    b = ''
    while n > 0:
        b = str(n%2) + b
        n = n // 2
    return print('Десятичное число', number, 'приобразованно в двоичное =', b)

finding_binar_number(int)