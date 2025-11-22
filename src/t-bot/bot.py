import telebot
import responses

bot = telebot.TeleBot("8265768086:AAHLg2UbVLfDNcKjQRib60scX9X-3hJRTVo")

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
