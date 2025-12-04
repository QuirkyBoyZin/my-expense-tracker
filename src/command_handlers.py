from helper import(
    validate_add
)


def handle_add(message):
    
    expense = message.text.split()
    validate_add(expense, message, handle_add)
    
    return
    ## Add into database