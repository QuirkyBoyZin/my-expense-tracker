from datetime import datetime
from t_bot import responses

# -------------------------------------------------------------
# /help
# -------------------------------------------------------------
def handle_help(response):
    return (
        "/help - Show all commands and descriptions\n"
        "/add <category> <name> <price> - Add an expense\n"
        "/view <date> - View expenses (defaults to today)\n"
        "/change <index> <name|price> - Change expense details\n"
        "/remove <index> - Remove an expense by index\n"
        "/end - End session\n"
    )

# -------------------------------------------------------------
# /add
# -------------------------------------------------------------
def handle_add(expense: list) -> tuple|str:
    if len(expense) < 4:
        return responses.MISSING_ARGUMENTS

    category = expense[1]
    name     = expense[2]
    price    = expense[3] 

    # Validate price
    try:
        price = float(expense[3])
    except:
        return responses.INVALID_PRICE

    return (category, name, price)

# -------------------------------------------------------------
# /view
# -------------------------------------------------------------
def handle_view(response, all_expenses):
    expense = response.split()
    date_filter = expense[1].strip() if len(expense) > 1 else None  # optional date

    filtered = []
    for item in all_expenses:
        date, _, exp = item
        if not date_filter or date == date_filter:
            filtered.append(item)

    if not filtered:
        return responses.EMPTY_LIST

    output = ""
    for i, item in enumerate(filtered, start=1):
        _, _, exp = item  # ignore date/time
        output += f"{i}. {exp.get_type()} {exp.get_name()} {exp.get_price()}$\n"

    return output.strip()

# -------------------------------------------------------------
# /change
# -------------------------------------------------------------
def handle_change(response, all_expenses):
    expense = response.split()

    if len(expense) < 3:
        return f"{handle_view(response, all_expenses)}\nUsage: /change <index> <name|price>"

    # convert index to int
    try:
        index = int(expense[1])
    except:
        return "Index must be a number."

    if index < 1 or index > len(all_expenses):
        return "Index out of range."

    field = expense[2].lower()

    if field not in ["name", "price"]:
        return "Choose either 'name' or 'price'."

    return (index, field)

# -------------------------------------------------------------
# /remove by index
# -------------------------------------------------------------
def handle_remove(response, all_expenses):
    expense = response.split()

    if len(expense) < 2:
        return "Usage: /remove <index>"

    try:
        index = int(expense[1])
    except:
        return "Index must be a number."

    if index < 1 or index > len(all_expenses):
        return "Index out of range."

    return index - 1  # zero-based index for bot.py

if __name__ == "__main__":
    pass