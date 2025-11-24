import telebot
import responses
import os
from dotenv import load_dotenv 

load_dotenv()
TOKEN         = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['add'])
def add(message):
    bot.reply_to(message, responses.SUCCESS)

@bot.message_handler(commands=['view'])
def view(message):
    bot.reply_to(message, responses.EMPTY)

@bot.message_handler(commands=['change'])
def change(message):
    bot.reply_to(message, responses.CHANGED)

@bot.message_handler(commands=['remove'])
def remove(message):
    bot.reply_to(message, responses.REMOVED)

@bot.message_handler(commands=['end'])
def end(message):
    bot.reply_to(message, responses.ENDED)

bot.polling()
