import os
from flask import Flask
import telebot
from telebot import types

API_TOKEN = '9238718427:AAF5QYEEofsLyzrP0dR191X6LAD9wcM4KHI'
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Aviochiptalar qidirish')
    btn2 = types.KeyboardButton('Visa murojaat')
    btn3 = types.KeyboardButton('Mehmonxona band qilish')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Salom! Kerakli bo'limni tanlang:", reply_markup=markup)

@app.route('/')
def home():
    return "Bot is running"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    bot.infinity_polling()
    
