# 6. Define a custom exception class and use it in a function to raise an exception under a specific condition.

def seven_input_not_allowed(num):
    if num == 7:
        raise Exception("Can't you f***ing read?!?!?!")
    print("You are smart!")

try:
    user_input = int(input("Enter any number EXCEPT 7: "))
    seven_input_not_allowed(user_input)

except Exception as e:
    print(e)
except:
    raise ValueError("Invalid input. Enter a valid number")