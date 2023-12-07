# 7. Develop a program that attempts to convert a user input to an integer, handling the ValueError if the input is not convertible.

try:
    user_input = input("Enter a number: ")
    user_input = int(user_input)
    print(f"{user_input} is a valid input.")
except ValueError:
    print("Input cannot be converted into int")
