from random import randint
import random

# задача 1. Создайте программу для игры с конфетами человек против бота.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 
# ...Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота

# а) Подумайте как наделить бота ""интеллектом""
def game(lot):
    try:
        print('Игра начинается')
        lot = input('Введите орел или решка\n')
        if lot == 'орел':
            print('Бот выбрал решку')
        elif lot == 'решка':
            print('Бот выбрал орел')
        if lot == 'орел' or lot == 'решка':
            print('Подкидываем монету')
            x = random.choice([True, False])
            if x == True and lot == 'орел':
                print('На монете выпал орел \nВы ходите первым')
                x = 1
            elif x==False and lot == 'решка':
                print('На монете выпала решка \nВы ходите первым')
                x = 1
            elif x == True and lot != 'орел':
                print('На монете выпал орел \nБот ходит первым')
                x = 0
            elif x ==False and lot != 'решка':
                print('На монете выпала решка \nБот ходит первым')
                x = 0
        player = 0
        bot = 0
        sum_player = 0
        sum_bot = 0
        if x == 1:
            apples = int(input('Введите количесво конфет на столе '))
            for i in range(apples):
                print(i+1, 'ход')
                player = int(input('Сколько конфет взять со стола '))
                if player > 28:
                    print('Вы взяли конфет больше чем можно по правилам \nВы проиграли ')
                    break
                apples -= player
                sum_player += player
                print(apples, 'Штук конфет осталось на столе')
                if apples == 0:
                    print('Вы выйграли')
                    print('Столько Конфет понадобилось для попеды', sum_player)
                    break
                if apples <= 28:
                    bot = apples
                    apples -= bot
                    sum_bot += bot
                    print('Бот взял', bot, 'Конфет')
                    print('Бот выйграл')
                    print('Столько конфет понадобилось для попеды', sum_bot)
                    break
                bot = (randint(1, 28))
                print('Бот взял', bot, 'конфет')
                apples -= bot
                sum_bot += bot
                print(apples, 'Штук конфет осталось на столе')
        else:
            apples = int(input('Введите количесво конфет на столе '))
            for i in range(apples):
                print(i+1, 'ход')
                if apples <= 28:
                    bot = apples
                    apples -= bot
                    sum_bot += bot
                    print('Бот взял', bot, 'Конфет')
                    print('Бот выйграл')
                    print('Столько конфет понадобилось для попеды', sum_bot)
                    break
                bot = (randint(1, 28))
                print('Бот взял', bot, 'Конфет')
                apples -= bot
                sum_bot += bot
                print(apples, 'Штук конфет осталось на столе')
                player = int(input('Сколько конфет взять со стола '))
                if player > 28:
                    print('Вы взяли конфет больше чем можно по правилам \nВы проиграли ')
                    break
                apples -= player
                sum_player += player
                print(apples, 'Штук конфет осталось на столе')
                if apples == 0:
                    print('Вы выйграли')
                    print('Столько конфет понадобилось для попеды', sum_player)
                    break
    except:
        print('Введены некорректные данные')

game('')

# задача 2.
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (здесь только буквы).
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def from_str_to_rlestr (x):
    string = x
    new_string = ''
    i = 0
    while i < len(string):
        count = 1
        while i+1 < len(string) and string[i] == string[i+1]:
            count += 1
            i += 1
        new_string += str(count) + string[i]
        i += 1
    print(new_string)
    f = open("TextRLE.txt", "w")
    f.write(new_string)
    return(new_string)

with open("Text.txt", "r") as f:
    text = f.read()

from_str_to_rlestr(text)

def from_rlestr_to_str (y):
    string = y
    new_string = ''
    i = 0
    while i < len(string):
        num = int(string[i])
        new_string += string[i+1]*num
        i+=2
    print(new_string)
    f = open("Text.txt", "w")
    f.write(new_string)
    return(new_string)

with open("TextRLE.txt", "r") as f:
    text = f.read()

from_rlestr_to_str (text)

#задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

text = 'привет абвдруг как твои делабв'
find = "абв"
def find_litters(text,find):
      split_text = text.split()
      new_list = []
      for i in range(len(split_text)):
            if not find in split_text[i]:
                  new_list.append(split_text[i])
      new_text = ' '.join(new_list)
      print(new_text)
      return new_text
find_litters(text,find)