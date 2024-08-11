class Calculator:
    def __init__(self) -> None:
        self.default_value = 0
    
    def add(self, number):
        result = self.default_value + number
        self.default_value = result
    
    def subtract(self, number):
        result = self.default_value - number
        self.default_value = result
    
    def divide(self, number):
        try:
            result = self.default_value / number
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        else:
            self.default_value = result
    
    def multiply(self, number):
        result = self.default_value * number
        self.default_value = result
    
    def reset(self) -> None:
        self.default_value = 0
        
    def get_current_value(self):
        return self.default_value
    
