from t_bot.bot import bot
from validate import(
    validate_add,
    validate_remove
)
from buttons import (
    make_btns
)
from state import user_state



commands = ('/add', '/view', '/remove','/change', '/help')

def handle_start(message):
    bot.send_message(message.chat.id, f'Here are a list of commands you can use', reply_markup= make_btns(*commands)) 
    return

def handle_add(message):
    chat_id = message.chat.id
    expense = message.text.split()
    valid = validate_add(expense, message, handle_add)
    
    if valid:
        bot.send_message(message.chat.id, f'What do you want to do next?', reply_markup= make_btns(*commands))
        user_state.pop(chat_id, None)

    return
    ## Add into database

def handle_view(message):
    pass

def handle_remove(message):
    chat_id = message.chat.id
    expense = message.text.split()
    valid = validate_remove(expense, message, handle_remove)
    
    if valid:
        bot.send_message(message.chat.id, f'What do you want to do next?', reply_markup= make_btns(*commands))
        user_state.pop(chat_id, None)
