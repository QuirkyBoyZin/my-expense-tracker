from t_bot.bot import bot
from validate import(
    validate_add
)
from buttons import (
    make_btns
)

commands = ('/add', '/view', '/remove','/change', '/help')

def handle_start(message):
    bot.send_message(message.chat.id, f'Here are a list of commands you can use', reply_markup= make_btns(*commands)) 
    return


def handle_add(message):

    expense = message.text.split()
    valid = validate_add(expense, message, handle_add)
    
    if valid:
        bot.send_message(message.chat.id, f'What do you want to do next?', reply_markup= make_btns(*commands))
    return
    ## Add into database

