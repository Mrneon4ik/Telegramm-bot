
from re import T
import telebot
from telebot import types

token='5749057194:AAE0AWDfVC88hfLFuLawb5O7rj9weqaMBYM'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    print(1)
    bot.send_message(message.chat.id,'Привет я bot_neon4ik могу помочь тебе найти прогноз погоды и узнать последние новости. Напиши /go для начала')

@bot.message_handler(commands=['go'])
def button_message(message):
    print(2)
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item2=types.KeyboardButton('погода')
    item3=types.KeyboardButton('новости')
    item4=types.KeyboardButton('YouTube')
    item6=types.KeyboardButton("test")
    item5=types.KeyboardButton("play market")
    markup.add(item2, item3, item4, item5, item6)
    bot.send_message(message.chat.id,'доступные команды смотрите ниже',reply_markup=markup)

@bot.message_handler(commands=['game'])
def button_message1(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item4=types.KeyboardButton('random')
    markup.add(item4)
    bot.send_message(message.chat.id,'для игры нажмите кнопку',reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    print(3)
    if message.text=="ознакомиться":
        bot.send_message(message.chat.id,'выберите ниже кнопки')
    elif message.text=='погода' and 'Погода':
        bot.send_message(message.chat.id, 'https://yandex.ru/pogoda/novouralsk?lat=57.247235&lon=60.095604')
    elif message.text=='YouTube':
         bot.send_message(message.chat.id,'m.youtube.com')
    elif message.text=='test':
        bot.send_message(message.chat.id, "пройден")
    elif message.text=='новости' and 'Новости':
        bot.send_message(message.chat.id, 'https://yandex.ru/news')
    elif message.text=='random':
        bot.send_message(message.chat.id, 'soon')
    else:
        bot.send_message(message.chat.id, 'повторите запрос')
        print(4)


bot.infinity_polling()


