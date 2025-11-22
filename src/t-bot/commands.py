from datetime import datetime
from models.expense import Expense


# -------------------------------------------------------------
# /help
# -------------------------------------------------------------
def handle_help(response):
    """
    Returns a list of all commands and their usage.
    """

    return (
        "/help - Show all commands\n"
        "/add <category> <name> <price> - Add an expense\n"
        "       Example: /add food burger 3.5\n"
        "/view <date> - View all expenses from a specific date\n"
        "       Example: /view 2024-11-22\n"
        "/change - Change an existing expense\n"
        "/remove - Remove an expense\n"
    )


# -------------------------------------------------------------
# /add
# -------------------------------------------------------------
def handle_add(response):
    """
    Handles adding an expense.
    Expected format:
        /add <category> <name> <price>
    Returns:
        [date, time, Expense(category, name, price)]
    """

    args = response.split()

    if len(args) < 4:
        return (
            "Missing arguments! Please follow:\n"
            "/add <category> <name> <price>"
        )

    category = args[1]
    name = args[2]

    # Validate price
    try:
        price = float(args[3])
    except:
        return "Price must be a number!"

    # Get date and time
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    expense_obj = Expense(category, name, price)

    return [date, time, expense_obj]


# -------------------------------------------------------------
# /view
# -------------------------------------------------------------
def handle_view(response, L):
    """
    Shows indexed list of expenses for a given date.
    Inputs:
        - response (string)
        - L (nested list) e.g. [ [Expense...], [Expense...] ]

    Output format:
        1. Food noodle 2.5
        2. Drinks coke 1.25
    """

    if not L:
        return "No expenses found for this date."

    output = ""

    for index, item in enumerate(L, start=1):
        # each item is a nested list like [ExpenseObj]
        expense = item[0]

        output += f"{index}. {expense.category} {expense.name} {expense.price}\n"

    return output.strip()


# -------------------------------------------------------------
# /change
# -------------------------------------------------------------
def handle_change(response, L):
    """
    Allows the user to modify an item.
    Steps:
        - Uses /view list to show items
        - User picks an index
        - Bot asks: "change name or price?"
        - Returns: (index, field_to_change)
    """

    # Expecting response like: "/change 2 name"
    args = response.split()

    if len(args) < 2:
        return "Please specify which item number to change."

    # user chooses index
    try:
        index = int(args[1])
    except:
        return "Invalid index. Please enter a number."

    if index < 1 or index > len(L):
        return "Index out of range."

    if len(args) == 2:
        return (
            "What do you want to change?\n"
            "Type one: name or price"
        )

    field = args[2].lower()

    if field not in ["name", "price"]:
        return "Invalid option. Choose 'name' or 'price'."

    # return the item index and field to change
    return (index, field)


# -------------------------------------------------------------
# /remove
# -------------------------------------------------------------
def handle_remove(response, L):
    """
    Removes an item from the list.
    Returns:
        (index, removed_item)
    """

    args = response.split()

    if len(args) < 2:
        return "Please specify which item number to remove."

    try:
        index = int(args[1])
    except:
        return "Invalid index."

    if index < 1 or index > len(L):
        return "Index out of range."

    removed_item = L[index - 1][0]

    # Return index + removed item
    return (index, removed_item)
