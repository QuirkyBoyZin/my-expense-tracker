import time
import reply
from t_bot.bot import bot

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

def validate_add(expense, message, func):

    if  len(expense)  < 3:

        bot.send_message(message.chat.id, reply.validate_add("missing_args", expense))
        bot.register_next_step_handler(message, func)
        return
    
    elif len(expense) > 3: 
        
        bot.send_message(message.chat.id, reply.validate_add("excessive_args", expense))
        bot.register_next_step_handler(message, func)
        return
    
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
    return