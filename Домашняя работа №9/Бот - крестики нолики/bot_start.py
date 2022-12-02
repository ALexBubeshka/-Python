import telebot
from who_win import *
from bot_move import *
from player_move import *
from field import *

API_TOKEN = '5827391755:AAE3_aQ9Mgj8jW-I4B48U5rbsOKHXS3j8Ms'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['game'])
def game(message):
      bot.send_message(message.chat.id,'Начнем игру в Крстики Нолики\nПравила игры: Вы должны вводить координаты от 0 до 2 по вертикали и горизонатали\n00 01 02\n10 11 12\n20 21 22')
      global field
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
