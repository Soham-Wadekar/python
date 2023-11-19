# 9. Create a program with a recursive function to calculate the sum of natural numbers.

def natural_number_sum(n):
    if n <= 0:
        return "Invalid Input. Enter a natural number!!"
    elif n == 1:
        return n
    else:
        return n + natural_number_sum(n-1)
    
num1 = 10
num2 = -23

print(f"The sum of {num1} is {natural_number_sum(num1)}")
print(f"The sum of {num2} is {natural_number_sum(num2)}")