from datetime import datetime
import time

from telebot import types
from g_sheets import sheets
from t_bot.bot    import bot
from cmd_handlers import(
    handle_help,
    handle_add,
    handle_view,
    handle_change,
    handle_remove
)
from t_bot import responses

date     = datetime.now().strftime("%Y-%m-%d")

# -------------------------------------------------------------
# Helper functions

def measure_perf(base_fn):
    """A decorator for measuring code execution time of a function"""
    def wrapper(*args):
        
        start_time   = time.perf_counter()
        result = base_fn(*args)
        end_time     = time.perf_counter()
        elasped_time = end_time - start_time
        
        print(f"Execution time for {base_fn.__name__}: {elasped_time:.3f} Seconds")
        return result
       
    return wrapper

def is_error (reply, message) -> bool:
    """ Validate messages"""
    if isinstance(reply, str):
        bot.reply_to(message, reply)
        return True
@measure_perf
def view_expense() -> str:
    """View expense for today"""
    expense_list      = sheets.get_expenses_at(date)
    user_expense_list = handle_view(expense_list)
    return user_expense_list

@measure_perf
def find_id(args) -> bool|int:
    """ Given an index find the corresponding ID returns false if not found"""
    expense = sheets.get_expenses_at(date)

    index = int(args[1]) - 1
    index_range = [i for i in range (len(expense))]
    
    if index not in index_range: return False
        
    id =  int(expense[index][0])
    return id
@measure_perf
def get_item(id) -> str:
    """ Given an id returns a string consists of the item's category name and price"""
    expense  =  sheets.get_item(id)
   
    
    category: str   =  expense[0]
    name:     str   =  expense[1]
    price:    float =  expense[2]
    
    return f"{category.capitalize()} {name.capitalize()} {price}" 




# -------------------------------------------------------------
# /start
# -------------------------------------------------------------
@bot.message_handler(commands=['start'])
@measure_perf
def start(message):
    bot.reply_to(message,
                 "👋 Hello! I'm your Expense Tracker Bot.\n"
                 "Use /help to see available commands.")

# -------------------------------------------------------------
# /help
# -------------------------------------------------------------
@bot.message_handler(commands=['help'])
@measure_perf
def help(message):
    reply = handle_help(message.text)
    bot.reply_to(message, reply)

# -------------------------------------------------------------
# /add
# -------------------------------------------------------------
@bot.message_handler(commands=['add'])
@measure_perf
def add(message):
    reply = message.text.split()
    category = reply[0]
    name     = reply[1]
    price    = reply[2]

    sheets.add_row(category, name, price)   
    id = len(sheets.get_expenses_at(date))                                                ##TODO: Use ✅  to show the recently added expense
    bot.reply_to(message, f"Sucessfully added item into your expense list:\n \t\t{get_item(id)}\n\n{view_expense()}")

# -------------------------------------------------------------
# /view: Provide a list of expense to the user 
## TODO:  Make it accepts an argument of a date and show the user the list of expense at that date
# -------------------------------------------------------------
@bot.message_handler(commands=['view'])
@measure_perf
def view(message):
    args = message.text.split()
    
    # Validating input
    if len(args) > 1:
        bot.reply_to(message, "This command doesn't accept argument.\n Usage: /view")
        return None
    
    bot.reply_to(message, view_expense())

# -------------------------------------------------------------
# /change
# -------------------------------------------------------------
@bot.message_handler(commands=['change'])
@measure_perf
def change(message):
   args = message.text.split()
   
   # User didn't enter any arguments
   if len(args) == 1:
        bot.reply_to(message,f"Which item do you want to change?\n\n{view_expense()}\nUsage: /change <index>") 
        return None
   global id
   id = int(args[1])
  
   
   markup = types.InlineKeyboardMarkup(row_width=1)
   
   category = types.InlineKeyboardButton('Category', callback_data= 'category')
   name     = types.InlineKeyboardButton('Name', callback_data= 'name')
   price    = types.InlineKeyboardButton('Price', callback_data= 'price')
   all      = types.InlineKeyboardButton('All', callback_data= 'all')
   markup.add(category, name, price, all)

   bot.send_message(message.chat.id, f'What do you want change for {get_item(id)}?', reply_markup= markup)

       
def change_name(message):
    name = message.text
    markup = types.InlineKeyboardMarkup(row_width=1)
    yes    = types.InlineKeyboardButton('Category', callback_data= 'yes')
    no     = types.InlineKeyboardButton('Name', callback_data= 'no')
     
    markup.add(yes,no)

    bot.send_message(message.chat.id, f'Are you sure?', reply_markup= markup)
    



def confirm_name(message):
     markup = types.InlineKeyboardMarkup(row_width=1)
     yes    = types.InlineKeyboardButton('Category', callback_data= 'yes')
     no     = types.InlineKeyboardButton('Name', callback_data= 'no')
     
     markup.add(yes,no)

     bot.send_message(message.chat.id, f'Are you sure?', reply_markup= markup)



@bot.callback_query_handler(func=lambda call: call.data == "name")
@measure_perf
def changed_name(callback):
    bot.send_message(callback.message.chat.id, "Enter new name")
    bot.register_next_step_handler(callback.message, change_name)
        

@bot.callback_query_handler(func=lambda call: call.data == "price")
@measure_perf
def change_price(callback):
    bot.send_message(callback.message.chat.id, "Enter new price")

@bot.callback_query_handler(func=lambda call: call.data == "yes")
@measure_perf
def confirm(callback):
     bot.send_message(callback.message.chat.id, "nice")



    
   




# -------------------------------------------------------------
# /remove
# -------------------------------------------------------------
@bot.message_handler(commands=['remove'])
@measure_perf
def remove(message):
    args = message.text.split()
    
    # User didn't enter any arguments
    if len(args) == 1:
        bot.reply_to(message,f"What do you want to remove?\n\n{view_expense()}\nUsage: /remove <index>") 
        return None
    
    id = find_id(args)
   
    if id is False:
        bot.reply_to(message,f"Invalid index\n\n{view_expense()}\nUsage: /remove <index>") 
        return None
    
    remove_item = get_item(id)
    sheets.remove_row(id)
    bot.reply_to(message,f"✅ Sucessfully removed:\n\n \t\t{remove_item} \n\n{view_expense()}") 
    
    return None
    

print("Bot is running...")
bot.infinity_polling()

# print(sheets.get_expenses_at("2025-12-02"))
# print(get_item(1))

