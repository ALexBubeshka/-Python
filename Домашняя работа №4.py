from random import randint
import random
# # задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def finding_list(n):
    try:
        n = int(input('Введите натуральное число - '))
        x = n
        list = []
        y = 2
        if n == 11 or n == 7 or n == 5 or n == 3 or n == 2 or n == 1:
            print(n, '- простое число')
        else:
            while n > 1:
                if n % y == 0:
                    n = n / y
                    list.append(y)
                else:
                    y += 1
            print('Список простых множителей', list, 'от числа', x)
        return list
    except:
        print('Введены некорректные данные')

finding_list('Введите натуральное число')

# задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def creacting_random_list(n):
    try:
        n = int(input('Введите длину списка '))
        list_numbers = []
        for i in range(n):
            list_numbers.append(randint(0, 10))
        return list_numbers
    except:
        print('Введены некорректные данные')
list = creacting_random_list('Введите длину списка ')

print(list)

def no_repiting_items(n):
    try:
        old_list = n
        new_list = []
        i = 0
        while i < len(old_list):
            if old_list.count(old_list[i]) > 1:
                i += 1
            else:
                new_list.append(old_list[i])
                i += 1
        if len(new_list) == 0:
            print('В списке нет неповторяющихся элементов ')
        else:
            return print('Список неповторяющихся элементов', new_list)
    except:
        print('Введены некорректные данные')

no_repiting_items(list)

# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def polynomial_list(k):
    try:
        k = int(input('Введите нутуральную степень '))
        list = []
        for i in range (0, k + 1):
            if k > 1: 
                list.append(random.randint(0, 101))
                list.append('x^')
                list.append(k)
                list.append('+')
                k -= 1

        list.append(random.randint(0, 101))
        list.append('x') 
        list.append('+')
        list.append(random.randint(0, 101))
        list.append('=')
        list.append('0')
        print(list)
        return ''.join(map(str, list))
    except:
         print('Введены некорректные данные')

poly = polynomial_list('Введите нутуральную степень ')

with open('Домашняя работа №4.txt', 'w') as data:
      data.write(poly)