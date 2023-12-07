def perform_division(dividend, divisor):
    try:
        result = dividend / divisor
        print(f"The result of {dividend} / {divisor} is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Please provide valid numeric inputs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
try:
    user_dividend = float(input("Enter the dividend: "))
    user_divisor = float(input("Enter the divisor: "))
    perform_division(user_dividend, user_divisor)
except ValueError:
    print("Invalid input. Please enter valid numeric values.")
