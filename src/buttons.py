from t_bot.bot import bot
from telebot import types


### Buttons for interaction

commands= ['/start', '/add', '/view', '/remove','/change', '/help']

container = types.InlineKeyboardMarkup(row_width=1)

add     = types.InlineKeyboardButton('Add',    callback_data= '/add')
view    = types.InlineKeyboardButton('View',   callback_data= '/view')
remove  = types.InlineKeyboardButton('Remove', callback_data= '/remove')
change  = types.InlineKeyboardButton('Change', callback_data= '/change')
help    = types.InlineKeyboardButton('Help',   callback_data= '/help')

btn = {'/add': add,'/view': view,'/remove': remove,'/change': change,'/help': help}


def next_step_btn(current_command):
    
    next_btns = []
    next_commands = commands.copy() 
    next_commands.remove(current_command)
    for command in next_commands:
        next_btns.append(btn[command])
    
    tuple(next_btns)    
    return container.add(*next_btns)


if __name__ == '__main__':
    
    # next_step_btn('/start')
    # after_start = container.add(add,view,remove,change,help)
    # after_start = next_step_btn('/start')
    pass



