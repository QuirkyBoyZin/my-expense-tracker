from t_bot.bot    import bot
import reply
from helper import(
    measure_perf
)
from command_handlers import(
    handle_warning,
    handle_start,
    handle_add,
)

commands= ['/start', '/add', '/view', '/remove','/change', '/help']

###-------------Validating Commands & Messages----------------###


def validate_message(message):
    """ Check if a given message from user is a command or not."""
    if message.text not in commands: return True
        
    return False

@bot.message_handler(func = validate_message)
@measure_perf
def warning(message):
    """ Shows a list of command to use if a user enter non-commands text"""
    handle_warning(message)
    return 
    

###--------------------------------------------------------------###

### Handling user's commands

@bot.message_handler(commands=['start','add','view', 'remove', 'change', 'help'])
@measure_perf
def command_handlers(message):
    
    if message.text == '/start':
        bot.send_message(message.chat.id, reply.WELCOME)
        handle_start(message)
        
        return
    
    elif message.text == "/add":
        bot.send_message(message.chat.id, reply.ADD_USAGE )
        bot.register_next_step_handler(message, handle_add)

        return
    
    elif message.text == "/view":
        bot.send_message(message.chat.id, reply.VIEW_USAGE )
        
        return
    
    elif message.text == "/remove":
        bot.send_message(message.chat.id, reply.REMOVE_USAGE )
        
        return
    
    elif message.text == "/change":
        bot.send_message(message.chat.id, reply.CHANGE_USAGE)
        
        return
    
    elif message.text == "/help":
        bot.send_message(message.chat.id, reply.HELP)
        
        return


### Users clicking on buttons
@bot.callback_query_handler(func= lambda call: call.data in commands )
@measure_perf
def handle_btn(callback):
    
    callback.message.text = callback.data # Changing the text attribute of message to commands (/add, /view...)
    command_handlers(callback.message)    # So, we can reuse code from command_handlers
       
    



print("Bot is running...")
bot.infinity_polling()
