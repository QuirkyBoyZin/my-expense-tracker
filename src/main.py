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

expenses = []
# -------------------------------------------------------------
# Helper functions
def is_error (reply, message) -> bool:
    if isinstance(reply, str):
        bot.reply_to(message, reply)
        return True

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

    expenses.append(reply)
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

    # Validate message
    if is_error(reply, message): return None

    index, field = reply
    bot.reply_to(message, f"You want to change item #{index}, field: {field}")

# -------------------------------------------------------------
# /remove
# -------------------------------------------------------------
@bot.message_handler(commands=['remove'])
def remove(message):
    reply = handle_remove(message.text, expenses)

    # Validate message
    if is_error(reply, message): return None

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