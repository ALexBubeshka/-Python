'''
Задание №1 
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
'''
n = int(input('Введите цифру обзназначающую день недели - '))
if n==6 or n==7:
    print('Выходной')
else:
    print('Не выходной')

'''
Задание №2
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
¬(X + Y + Z) = ¬X * ¬Y * ¬Z
не (X или Y или Z) = не X и не Y и не Z 
'''
x = bool(input('True или False  - '))
y = bool(input('True или False  - '))
z = bool(input('True или False  - '))

if -(x+y+z)==-x*-y*-z:
    print('утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z Верно')
else:
    print('утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  Не верно')



'''
Задание №3
Напишите программу, которая принимает на вход координаты точки (X и Y), 
и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
'''