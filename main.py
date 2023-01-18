import os
import telebot
from flask import Flask, request

TOKEN = '5904550329:AAEwOCL3jszxaos0s-7EVQGXe_Bz0uvSyYM'
APP_URL = f'https://bot1-lv71sg8gw-dimamatuh.vercel.app/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo(message):
    bot.reply_to(message, message.text)


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return'!', 200


bot.polling(none_stop=True)


input()