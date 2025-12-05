import reply
from t_bot.bot import bot
from helper import(
    find_id
)

def validate_add(expense, message, func) -> bool:
    """ Validate expense before adding if passes return true else send 
        a message to user about their mistake"""

    # Missing arguments
    if  len(expense)  < 3:

        bot.send_message(message.chat.id, reply.validate_add("missing_args", expense))
        bot.register_next_step_handler(message, func)
        return
    
    # Excessive arguments
    elif len(expense) > 3: 
        
        bot.send_message(message.chat.id, reply.validate_add("excessive_args", expense))
        bot.register_next_step_handler(message, func)
        return
    
    # Checking if category is string, name is string and price is a float
    invalid_category = True
    invalid_name     = True
    invalid_price    = False
    
    category: str    = expense[0]
    name:     str    = expense[1]
    price:    float  = expense[2]
    
    try:
        float(category)
    except ValueError:
        invalid_category = False
    
    try:
        float(name)
    except ValueError:
        invalid_name = False
    
    try:
        float(price)
    except ValueError:
        invalid_price = True
    
      
    if invalid_category:
        
        bot.send_message(message.chat.id, reply.validate_add('category', expense))
        bot.register_next_step_handler(message, func)  
        return
 
    elif invalid_name:
        
        bot.send_message(message.chat.id, reply.validate_add('name', expense))
        bot.register_next_step_handler(message, func)  
        return
    
    elif invalid_price:
        
        bot.send_message(message.chat.id, reply.validate_add('price', expense))
        bot.register_next_step_handler(message, func)
        return
    
    bot.send_message(message.chat.id, reply.validate_add('success', expense))
    return True

def validate_remove(message, func) -> tuple[bool,int]:
    """ Validate before removing if passes return true else send 
        a message to user about their mistake"""
    
    # Checking if index is an int
    invalid_index = False
    try:
        index = int(message.text)
    except ValueError:
        invalid_index = True

    if invalid_index:
        bot.send_message(message.chat.id, reply.validate_remove("text", message.text))
        bot.register_next_step_handler(message, func)
        return
   
    # index must be [1, len(list of expense)]
    (id, msg) = find_id(index)
    if id is False:
        bot.send_message(message.chat.id, reply.validate_remove("id", msg))
        bot.register_next_step_handler(message, func)
        return
    
    bot.send_message(message.chat.id, reply.validate_remove('success', message.text))
    return (True, id)