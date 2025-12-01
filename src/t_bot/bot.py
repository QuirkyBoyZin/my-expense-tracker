import os
from dotenv import load_dotenv
import telebot
from .commands import (
    handle_help,
    handle_add,
    handle_view,
    handle_change,
    handle_remove
)
from . import responses

load_dotenv()
TOKEN    = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
bot = telebot.TeleBot(TOKEN)

# This stores all expense entries
# Format: [date, time, Expense object]
def start():
    expenses = []

    # -------------------------------------------------------------
    # /start
    # -------------------------------------------------------------
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.reply_to(message,
                    "👋 Hello! I'm your Expense Tracker Bot.\n"
                    "Use /help to see available commands.")

    # -------------------------------------------------------------
    # /help
    # -------------------------------------------------------------
    @bot.message_handler(commands=['help'])
    def help(message):
        reply = handle_help(message.text)
        bot.reply_to(message, reply)

    # -------------------------------------------------------------
    # /add
    # -------------------------------------------------------------
    @bot.message_handler(commands=['add'])
    def add(message):
        result = handle_add(message.text)

        if isinstance(result, str):
            bot.reply_to(message, result)
            return

        expenses.append(result)
        bot.reply_to(message, responses.SUCCESS)

    # -------------------------------------------------------------
    # /view
    # -------------------------------------------------------------
    @bot.message_handler(commands=['view'])
    def view(message):
        reply = handle_view(message.text, expenses)
        bot.reply_to(message, reply)

    # -------------------------------------------------------------
    # /change
    # -------------------------------------------------------------
    @bot.message_handler(commands=['change'])
    def change(message):
        reply = handle_change(message.text, expenses)

        if isinstance(reply, str):
            bot.reply_to(message, reply)
            return

        index, field = reply
        bot.reply_to(message, f"You want to change item #{index}, field: {field}")

    # -------------------------------------------------------------
    # /remove
    # -------------------------------------------------------------
    @bot.message_handler(commands=['remove'])
    def remove(message):
        reply = handle_remove(message.text, expenses)

        if isinstance(reply, str):
            bot.reply_to(message, reply)
            return

        removed_item = expenses.pop(reply)[2]  # remove by index
        bot.reply_to(message, f"Removed: {removed_item.name} ✔")

    # -------------------------------------------------------------
    # /end
    # -------------------------------------------------------------
    @bot.message_handler(commands=['end'])
    def end(message):
        expenses.clear()
        bot.reply_to(message, responses.ENDED)

    print("Bot is running...")
    bot.polling(none_stop=True)

if __name__ == "__main__":
    start()
    pass