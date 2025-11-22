import telebot
import responses
import command

bot = telebot.TeleBot("8265768086:AAHLg2UbVLfDNcKjQRib60scX9X-3hJRTVo") 

# Store all expenses in a nested list
expenses_list = []

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, command.handle_help(message.text))

@bot.message_handler(commands=['add'])
def add_command(message):
    result = command.handle_add(message.text)
    if isinstance(result, list):
        # result = [date, time, ExpenseObj]
        expenses_list.append([result[2]])  # store only Expense object in nested list
        bot.reply_to(message, responses.SUCCESS)
    else:
        bot.reply_to(message, result)  # error message

@bot.message_handler(commands=['view'])
def view_command(message):
    output = command.handle_view(expenses_list, expenses_list)
    bot.reply_to(message, output)

@bot.message_handler(commands=['change'])
def change_command(message):
    result = command.handle_change(message.text, expenses_list)
    if isinstance(result, tuple):
        index, field = result
        bot.reply_to(message, f"Ready to change item {index}'s {field}.")
    else:
        bot.reply_to(message, result)

@bot.message_handler(commands=['remove'])
def remove_command(message):
    result = command.handle_remove(message.text, expenses_list)
    if isinstance(result, tuple):
        index, removed_item = result
        expenses_list.pop(index - 1)
        bot.reply_to(message, responses.REMOVED)
    else:
        bot.reply_to(message, result)

@bot.message_handler(commands=['end'])
def end_command(message):
    bot.reply_to(message, responses.ENDED)

bot.polling()

