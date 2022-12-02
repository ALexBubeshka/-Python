import field
import telebot

API_TOKEN = '5827391755:AAE3_aQ9Mgj8jW-I4B48U5rbsOKHXS3j8Ms'
bot = telebot.TeleBot(API_TOKEN)

# @bot.message_handler(content_types=['text'])
def player_move (field_print):
      global message
      try:
            # bot.send_message(message.chat.id, "Введите координаты")  # В этом месте он не останавливается для получения данных от пользователя
            move = input('c')
            move_coord = move.split(',')
            x = int(move_coord[0])
            y = int(move_coord[1])
            if field.field[x][y] == 'X' or field.field[x][y] == 'O':
                  print('пропуск хода')
                  # bot.send_message(message.chat.id,'Пропускаете свой ход по причине ввода некорректных данных')
                  return field_print
            else:
                  field.field [x][y] = 'X'
                  return field_print
      except:
            # bot.send_message(message.chat.id,'Пропускаете свой ход по причине ввода некорректных данных')
            print('пропуск хода')
            return field_print