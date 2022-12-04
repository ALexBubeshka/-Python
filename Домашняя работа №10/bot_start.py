import telebot
from telebot import types
from reading_json import data
from del_json import *
from searching_json import *

API_TOKEN = '5827391755:AAE3_aQ9Mgj8jW-I4B48U5rbsOKHXS3j8Ms'

new_empl_info = {}
keys = []
phones = []

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
      global fieldValues
      global exempl_1
      global new_employee
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton('Полная база данных')
      btn2 = types.KeyboardButton('Добавить работника')
      btn3 = types.KeyboardButton('Удалить работника')
      btn4 = types.KeyboardButton('Поиск')
      markup.add(btn1, btn2,btn3,btn4)
      bot.send_message(message.chat.id, text="Привет, {0.first_name}! Добро пожаловать в базу данных работников".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
      if(message.text == 'Полная база данных'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(back)
            bot.send_message(message.chat.id, text=json.dumps(data, indent=4, sort_keys=True), reply_markup=markup)
      elif(message.text == 'Добавить работника'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(back)
            msg = bot.send_message(message.chat.id, 'Введите ФИО нового работника', reply_markup=markup)
            bot.register_next_step_handler(msg, fio_empl)
      elif(message.text == 'Удалить работника'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(back)
            msg = bot.send_message(message.chat.id, 'Введите ФИО работника доя удаления из базы', reply_markup=markup)
            bot.register_next_step_handler(msg, del_worker)
      elif(message.text == 'Поиск'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(back)
            msg = bot.send_message(message.chat.id, "Введите данные сотрудника.", reply_markup=markup)
            bot.register_next_step_handler(msg, search_empl_json)
      elif (message.text == "Вернуться в главное меню"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Полная база данных')
            btn2 = types.KeyboardButton('Добавить работника')
            btn3 = types.KeyboardButton('Удалить работника')
            btn4 = types.KeyboardButton('Поиск')
            markup.add(btn1,btn2,btn3,btn4)
            bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
      else:
            bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")

def del_worker (message):
      try:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(back)
            exempl_1 = message.text
            del_el(exempl_1)   
            bot.send_message(message.chat.id, text='Работник был удален')
      except:
            bot.send_message(message.chat.id, text='Такого работника нет в базе данных')

def search_empl_json(message):
    msg = message.text
    searching_el(msg)
    bot.send_message(message.chat.id, json.dumps(results, indent=4))

def fio_empl(message):
    global new_empl_info
    new_empl_info['Full name'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите пол (F / M) нового работника')
    bot.register_next_step_handler(msg, sex_empl)

def sex_empl(message):
    new_empl_info['Sex'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите дату рождения нового работника (dd.mm.year)')
    bot.register_next_step_handler(msg, age_empl)

def age_empl(message):
    new_empl_info['Birth date'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите семейное положение нового работника')
    bot.register_next_step_handler(msg, marital_status_empl)

def marital_status_empl(message):
    new_empl_info['Marital status'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите должность нового работника')
    bot.register_next_step_handler(msg, job_title_empl)

def job_title_empl(message):
    new_empl_info['Job title'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите заработную плату нового работника')
    bot.register_next_step_handler(msg, salary_empl)

def salary_empl(message):
    new_empl_info['salary'] = int(message.text)
    msg = bot.send_message(message.chat.id, 'Введите первый телефонный номер нового работника')
    bot.register_next_step_handler(msg, phone_1)

def phone_1(message):
    global phones
    ph_1 = message.text
    phones.append(int(ph_1))
    msg = bot.send_message(message.chat.id, 'Введите второй телефонный номер нового работника')
    bot.register_next_step_handler(msg, phone_2)

def phone_2(message):
    global phones
    ph_2 = message.text
    phones.append(int(ph_2))
    ending_dict(message)

def ending_dict(message):
    new_empl_info['Phone numbers'] = phones
    adding_id(message)

def adding_id(message):
    with open('employees.json', 'r') as file:
        data = json.load(file)
        for k, v in data.items():
            keys.append(k)
    new_empl_key = int(keys[-1]) + 1
    data[new_empl_key] = new_empl_info
    with open('employees.json', 'w')as file:
        json.dump(data, file, indent=4)
    bot.send_message(message.chat.id, "Новый сотрудник добавлен.")
    bot.send_message(message.chat.id, json.dumps(data, indent=4))

bot.polling()
