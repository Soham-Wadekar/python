# 4. Develop a program that takes user input for an integer and handles the case when non-integer input is provided.

try:
    user_input = int(input("Enter an integer: "))
    print(f"{user_input} is a valid integer")
except ValueError:
    print("Input must be an integer")
