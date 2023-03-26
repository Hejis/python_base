import telebot
import random

from les4 import pars

token = ''

bot = telebot.TeleBot(token)

number = 0


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Рандомное число')
    item2 = telebot.types.KeyboardButton('Знак зодиака')
    

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'отлично':
        bot.send_message(message.chat.id, 'Я рад за тебя')
    elif message.text.lower() == 'плохо':
        bot.send_message(message.chat.id, 'Что случилось?')
    
    elif message.text.lower() == 'знак зодиака':
        markup = telebot.types.ReplyKeyboardMarkup(row_width=4)
        item1 = telebot.types.KeyboardButton('Овен')
        item2 = telebot.types.KeyboardButton('Телец')
        item3 = telebot.types.KeyboardButton('Близнецы')
        item4 = telebot.types.KeyboardButton('Рак')
        item5 = telebot.types.KeyboardButton('Лев')
        item6 = telebot.types.KeyboardButton('Козерог')
        item7 = telebot.types.KeyboardButton('Весы')
        item8 = telebot.types.KeyboardButton('Скорпион')
        item9 = telebot.types.KeyboardButton('Водолей')
        item10 = telebot.types.KeyboardButton('Стрелец')
        item11 = telebot.types.KeyboardButton('Дева')
        item12 = telebot.types.KeyboardButton('Рыбы')
        item13 = telebot.types.KeyboardButton('Назад')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)
        bot.send_message(message.chat.id, 'Жмакни на кнопку', reply_markup=markup)
        bot.register_next_step_handler(message, horoscope)
    elif message.text.lower() == 'рандомное число':
        bot.send_message(message.chat.id, str(random.randint(1, 100)))
    

@bot.message_handler(content_types=['text'])
def horoscope(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=4)
    item1 = telebot.types.KeyboardButton('Овен')
    item2 = telebot.types.KeyboardButton('Телец')
    item3 = telebot.types.KeyboardButton('Близнецы')
    item4 = telebot.types.KeyboardButton('Рак')
    item5 = telebot.types.KeyboardButton('Лев')
    item6 = telebot.types.KeyboardButton('Козерог')
    item7 = telebot.types.KeyboardButton('Весы')
    item8 = telebot.types.KeyboardButton('Скорпион')
    item9 = telebot.types.KeyboardButton('Водолей')
    item10 = telebot.types.KeyboardButton('Стрелец')
    item11 = telebot.types.KeyboardButton('Дева')
    item12 = telebot.types.KeyboardButton('Рыбы')
    item13 = telebot.types.KeyboardButton('Назад')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)
    if message.text != 'Назад':
        bot.send_message(message.chat.id, pars(message.text), reply_markup=markup)
        bot.register_next_step_handler(message, horoscope)
    elif message.text == 'Назад':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('Рандомное число')
        item6 = telebot.types.KeyboardButton('Знак зодиака')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)

bot.polling(none_stop=True)