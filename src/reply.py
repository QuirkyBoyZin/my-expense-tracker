#### Constants or functions for replying message to user ####

### Warning message if user enter anything other than the list of commands that can be used

WARNING = f"I can only that track your expense. Here is a list of commands you can use"

### Using /start

WELCOME = f"Hey, I am your expense tracker. Ready to log in?"

### Using /add

ADD_USAGE = ("Please enter your expense in this format:\n\n"
               "Format:  \t\t\t\t\t\t Type       Name      Price in (USD)\n"
               "Exmaple:       Food      Noodle           2.5" )

def validate_add(condition: str, message: list) -> str:
    """ Validating /add cammand returns a validation message.\n
        condition's arguments:\n 
        success\n
        missing_args\n
        excessive_args\n
        category\n
        name\n
        price\n
    """
    if len(message) == 3:
        category = message[0]
        name     = message[1]
        price    = message[2]

    if condition == "success":
        recently_added = f"{category} {name} {price}"
        return f"Sucessfully added {recently_added}  to your list of expense" 
    
    elif condition == "missing_args":
        return (f"Missing arguments for {" ".join(message)}. \n\n"
                    "Usage:  \t\t\t\t\t\t\t\t Type       Name      Price in (USD)\n"
                    "Exmaple:       Food      Noodle           2.5" )
    
    elif condition == "excessive_args":
         return (f"Excessive arguments for {" ".join(message)}. \n\n"
                    "Usage:  \t\t\t\t\t\t\t\t Type       Name      Price in (USD)\n"
                    "Exmaple:       Food      Noodle           2.5" ) 

    elif condition == "category":
        return f"Invalid Category: {category}. Please enter text" 

    elif condition == "name":
        return f"Invalid Name: {name}. Please enter text"

    elif condition == "price":
        return f"Invalid Price: {price}. Please enter numbers"
    
    else: 
        return f"Error, Please try again."


### Using /view

VIEW_USAGE  = "Here is your list of expenses for today"

### Using /remove

REMOVE_USAGE = "Which item do you want to remove?\n"

### Using /change

CHANGE_USAGE = "Which item do you want to change?\n"

### Using /help

HELP = (
            "/add:    \t\t\t\t\t\t Add an item to your expense\n\n"
            "/view:   \t\t\t\t\t\t View your expense list\n\n"
            "/remove: \t\t Remove an item in your expense list\n\n"
            "/change: \t\t Changing an item in your expense\n\n"
            "/help:   \t\t\t\t\t\t Show a list of commands\n\n")




if __name__ == "__main__":
    # print(add_successful(['food', 'noodle', '2.5']))
    pass