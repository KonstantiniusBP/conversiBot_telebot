import os
import telebot
from telebot import types
import requests

import conf

bot = telebot.TeleBot(conf.config['token'])

@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Конвертировать YouTube видео в mp3')
    kb.add(button1)
    bot.send_message(message.chat.id, 'Привет!', reply_markup=kb)

bot.polling()