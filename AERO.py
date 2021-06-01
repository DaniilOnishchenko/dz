# Кейс: Разработка чат бота для навигации пассажира в аэропорту «Краснодар»
 
# 1) Приветствие пассажира, информация о боте. Кнопки для выбора нужного объекта

# -Регистрация
# -Регистрация на стойке самообслуживания
# -Аптека
# -Кафе
# -Бизнес-зал
# -Проход на досмотр
# -Выход из аэропорта

# 2)
# -При выборе коммерческих строк предоставляется лист вариантов (кафе, аптеки и т.д)
# -При выборе бизнес-зала предоставляется возможность построить маршрут 
# -При выборе прочих вариантов предлагается построить маршрут

# 3)
# -При выборе кафе/аптек предоставляется информация о среднем чеке и типе кухни


# 4)
# При окончательном выборе кафе предлагает забронировать столик для этого просит ввести номер телефона и время прихода

import telebot
from telebot import types

TOKEN = '1811415738:AAERwHlquzMu5syFJQKdWzHVhcjzcIKSOGw'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help'])
def help_def(message):
    bot.send_message(message.from_user.id, "Напиши Привет")

@bot.message_handler(content_types=['text']) 
def get_text_messages(message): 
    if message.text == "Привет": 
        main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        button1 = types.KeyboardButton('Кафе')
        button2 = types.KeyboardButton('Бизнес-зал') 
        button3 = types.KeyboardButton('Аптека')
        button4 = types.KeyboardButton('Регистрация')
        button5 = types.KeyboardButton('Саморегистрация')

        main_markup.add(button1, button2, button3, button4, button5)
        bot.send_message(message.chat.id, "Привет, я бот Аэропорта 'Краснодар'. \nВыбери нужную кнопку и я помогу тебе. ", reply_markup = main_markup)
    else: 
        bot.send_message(message.chat.id, "Я тебя не понимаю. напиши /help.")

bot.polling()
