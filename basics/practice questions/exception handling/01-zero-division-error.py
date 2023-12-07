# 1. Create a function for dividing two numbers, handling the case of division by zero using exception handling.


def divide(x, y):
    try:
        return x / y
    except:
        return "Cannot divide by zero"


quotient1 = divide(10, 3)
print(quotient1)

quotient2 = divide(4, 0)
print(quotient2)
