'''A module with basic mathematical operations'''

def add(num1, num2):
    '''Adds two numbers'''
    return num1 + num2

def subtract(num1, num2):
    '''Subtracts two numbers'''
    return num1 - num2

def multiply(num1, num2):
    '''Multiplies two numbers'''
    return num1 * num2

def divide(num1, num2):
    '''Divides two numbers'''
    if num2 == 0:
        raise ValueError('Cannot divide by zero!')
    return num1 / num2
