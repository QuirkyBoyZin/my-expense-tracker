from t_bot.bot import bot
from validate import(
    validate_add
)
from buttons import (
    next_step_btn
)

def handle_warning(message):
    bot.send_message(message.chat.id, f'Here are a list of commands you can use', reply_markup= next_step_btn('/start'))
    return

def handle_start(message):
    bot.send_message(message.chat.id, f'Here are a list of commands you can use', reply_markup= next_step_btn(message.text))
    return


def handle_add(message):
    expense = message.text.split()
    validate_add(expense, message, handle_add)
    
    return
    ## Add into database

