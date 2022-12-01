from input import *
from out import *
from out import result_output
from rational_calc import *
import telebot

var1 = ''

API_TOKEN = '5827391755:AAE3_aQ9Mgj8jW-I4B48U5rbsOKHXS3j8Ms'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['game'])
def game(message):
      bot.send_message(message.chat.id,'Добро пожаловать в калькулятор\nВведите данные')

@bot.message_handler(content_types=['text'])
def message_reply(message):
      global var1
      var1 = message.text
      input_numbers(message.text)
      bot.send_message(message.chat.id,'Решение: ' + message.text + ' = ' + str(result_output(ration_nums, el_1, el_3, el_4)))

bot.polling()
