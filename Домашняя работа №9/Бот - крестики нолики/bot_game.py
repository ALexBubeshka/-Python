import random
import telebot

# Задача 2. Создайте программу для игры в "Крестики-нолики"в телеграм боте.

API_TOKEN = '5827391755:AAE3_aQ9Mgj8jW-I4B48U5rbsOKHXS3j8Ms'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['game'])
def game(message):

      field = []
      def print_field (field_print):
            f1 = ''
            for i in range (3):
                  print("  ".join(field_print[i]))
                  f1 +="  ".join(field_print[i])
                  f1 += '\n'
            bot.send_message(message.chat.id,f1)      
            return f1

      for i in range (3):
            fieldrow = []
            for j in range (3):
                  fieldrow.append ('-')
            field.append (fieldrow)

      def comp_move (field_print):
            bot.send_message(message.chat.id,'ходит бот')
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
                        bot.send_message(message.chat.id,'Вы выйграли')
                        a = True
                  else:
                        bot.send_message(message.chat.id,'Бот выйграл')
                        a = True
            elif field[0][0]==field[1][0]==field[2][0]==a or field[0][1]==field[1][1]==field[2][1]==a  or field[0][2]==field[1][2]==field[2][2]==a :
                  if a == 'X':
                        bot.send_message(message.chat.id,'Вы выйграли')
                        a = True
                  else:
                        bot.send_message(message.chat.id,'Бот выйграл')
                        a = True
            elif field[0][0]==field[1][1]==field[2][2]==a or field[0][2]==field[1][1]==field[2][0]==a:
                  if a == 'X':
                        bot.send_message(message.chat.id,'Вы выйграли')
                        a = True
                  else:
                        bot.send_message(message.chat.id,'Бот выйграл')
                        a = True
            return a


      def player_move (field_print):
            try:   
                  # bot.send_message(message.chat.id, "Введите координаты")  # В этом месте он не останавливается для получения данных от пользователя
                  move_coord = message.text.split(',')
                  x = int(move_coord[0])
                  y = int(move_coord[1])
                  if field[x][y] == 'X' or field[x][y] == 'O':
                        bot.send_message(message.chat.id,'Пропускаете свой ход по причине ввода некорректных данных')
                        return field_print
                  else:
                        field [x][y] = 'X'
                        return field_print
            except:
                  bot.send_message(message.chat.id,'Пропускаете свой ход по причине ввода некорректных данных')
                  return field_print

      bot.send_message(message.chat.id,'Начнем игру в Крстики Нолики')
      bot.send_message(message.chat.id,'Правила игры: Вы должны вводить координаты от 0 до 2 по вертикали и горизонатали\n00 01 02\n10 11 12\n20 21 22')
      for m in range (10):
            if m == 9:
                  bot.send_message(message.chat.id,'Ничья')
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


bot.polling()