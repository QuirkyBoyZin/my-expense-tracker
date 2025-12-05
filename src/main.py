from t_bot.bot    import bot
import reply
from helper import(
    measure_perf
)
from command_handlers import(
    handle_start,
    handle_add,
)
from state import user_state

commands= ['/start', '/add', '/view', '/remove','/change', '/help']

  
@bot.message_handler(func= lambda msg: msg.text not in commands)  # Validating Commands & Messages
@measure_perf
def warning(message):
    """ Shows a list of command to use if a user enter non-commands text"""
    handle_start(message)
    return 
    

###--------------------------------------------------------------###

### Handling user's commands

@bot.message_handler(commands=['start','add','view', 'remove', 'change', 'help'])
@measure_perf
def command_handlers(message):
    
    if message.text == '/start':
        # Welcomes user and show a list of commands to use
        bot.send_message(message.chat.id, reply.WELCOME)
        handle_start(message)
        
        return
    
    elif message.text == "/add":
        # Let user add their expense 
        chat_id = message.chat.id
        user_state[chat_id] = "add"   # ✅ set state
        
        bot.send_message(message.chat.id, reply.ADD_USAGE )
        bot.register_next_step_handler(message, handle_add)
        return
    
    elif message.text == "/view":
        bot.send_message(message.chat.id, reply.VIEW_USAGE )
        
        return
    
    elif message.text == "/remove":
        chat_id = message.chat.id
        user_state[chat_id] = "remove"   # ✅ set state
        bot.send_message(message.chat.id, reply.REMOVE_USAGE )
        
        return
    
    elif message.text == "/change":
        bot.send_message(message.chat.id, reply.CHANGE_USAGE)
        chat_id = message.chat.id
        user_state[chat_id] = "change"   # ✅ set state
        return
    
    elif message.text == "/help":
        bot.send_message(message.chat.id, reply.HELP)
        
        return


### Users clicking on buttons
@bot.callback_query_handler(func= lambda call: call.data in commands )
@measure_perf
def handle_btn(callback):

    chat_id = callback.message.chat.id
    # check if this user is currently in an active flow
    if user_state.get(chat_id) is None:
        # user is free, proceed
        callback.message.text = callback.data
        command_handlers(callback.message)
    else:
        # user is mid-flow, block button
        bot.answer_callback_query(callback.id,  "❗ Please finish this task first.")
        
           
   


print("Bot is running...")
bot.infinity_polling()
