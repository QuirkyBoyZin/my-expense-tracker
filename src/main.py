from datetime import datetime

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
def is_error (reply, message) -> bool:
    """ Validate messages"""
    if isinstance(reply, str):
        bot.reply_to(message, reply)
        return True

def view_expense() -> str:
    """View expense for today"""
    expense_list      = sheets.get_expenses_at(date)
    user_expense_list = handle_view(expense_list)
    return user_expense_list

def find_id(args) -> bool|int:
    """ Given an index find the corresponding ID returns false if not found"""
    expense = sheets.get_expenses_at(date)
    all_index = len(expense)
    index = int(args[1]) - 1
    
    if index > all_index or index < 0:
        return False
    
    id =  int(expense[index][0])
    return id

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
    reply = handle_add((message.text).split())

    # Validate message
    if is_error(reply, message): return None
    
    # Turns reply to an expense if reply isn't a string
    category = reply[0]
    name     = reply[1]
    price    = reply[2]

    sheets.add_row(category, name, price)                                  ##TODO: Use ✅  to show the recently added expense
    bot.reply_to(message, f"Sucessfully added item into your expense list:\n\n{view_expense()}")

# -------------------------------------------------------------
# /view: Provide a list of expense to the user 
## TODO:  Make it accepts an argument of a date and show the user the list of expense at that date
# -------------------------------------------------------------
@bot.message_handler(commands=['view'])
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
def change(message):
    reply = handle_change(message.text)

    # Validate message
    if is_error(reply, message): return None

    index, field = reply
    bot.reply_to(message, f"You want to change item #{index}, field: {field}")

# -------------------------------------------------------------
# /remove
# -------------------------------------------------------------
@bot.message_handler(commands=['remove'])
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
bot.polling(none_stop=True)

# print(sheets.get_expenses_at("2025-12-02"))
# print(get_item(1))

