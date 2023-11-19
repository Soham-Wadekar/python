# 1. Implement a program with a function that calculates the factorial of a given number.

def factorial(n):
    if n < 0:
        return "Factorial of a negative number cannot be calculated"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
num1 = 10
num2 = 0
num3 = -10

print(f"Factorial of {num1} = {factorial(num1)}")
print(f"Factorial of {num2} = {factorial(num2)}")
print(f"Factorial of {num3} = {factorial(num3)}")