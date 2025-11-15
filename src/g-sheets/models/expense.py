class Expense(object):
    def __init__(self, type: str, name:str , price: float):
        self.type  = type
        self.name  = name
        self.price = price
        if   not isinstance(self.type,str) :
            raise TypeError(f"Only strings are allowed\n~~~~{type} is not allowed~~~~")
        elif not isinstance(self.name,str):
            raise TypeError(f"Only strings are allowed\n~~~~{name} is not allowed~~~~")
        elif not isinstance(self.price, float):
            raise TypeError(f"Only floats are allowed\n~~~~{price} is not allowed~~~~")
        return self.type
    def get_type(self):
        return self.type
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def __str__(self):
        return f"Type of item: {self.type}\nName of item: {self.name}\nPrice of item: {self.price}"
    



if __name__ == '__main__': 
    pass