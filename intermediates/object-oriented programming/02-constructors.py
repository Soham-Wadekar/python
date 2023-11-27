# The __init__() method is a constructor of the class and it is called when the class is created

# The __init__() function is used to assign values to object properties, or other operations that are necessary to do when the object is being created

class Operations:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y
    
    def multiply(self):
        return self.x * self.y
    
    def divide(self):
        try:
            return self.x / self.y
        except ZeroDivisionError as e:
            print("Cannot divide by zero")
            print(e)
        except ValueError as e:
            print("Value must be integer or float")
            print(e)
    
    def modulo(self):
        try:
            return self.x % self.y
        except ZeroDivisionError as e:
            print("Cannot divide by zero")
            print(e)
        except ValueError as e:
            print("Value must be integer or float")
            print(e)

    def custom_num(self, y):
        self.y = y
        return self.y


x, y = 10, 3
obj = Operations(x,y)

print(f"{x} + {y} = {obj.add()}")
print(f"{x} - {y} = {obj.subtract()}")
print(f"{x} * {y} = {obj.multiply()}")
print(f"{x} / {y} = {obj.divide()}")
print(f"{x} % {y} = {obj.modulo()}")
print(f"{x} + {obj.custom_num(100)} = {obj.add()}")