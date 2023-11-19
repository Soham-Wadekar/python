# 2. Implement a program to calculate the factorial of a given positive integer using a loop.

num = 5
fact = 1

if num < 0:
    print("Invalid input")
elif num == 0 or num == 1:
    print(f"Factorial of {num} = {1}")
else:
    for i in range(1,num+1):
        fact *= i
    print(f"Factorial of {num} = {fact}")
