# 6. Create a function to find the greatest common divisor (GCD) of two numbers using Euclid's algorithm.


def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return abs(num1)


num1 = 70
num2 = 15

num3 = 19
num4 = 57

print(f"GCD of {num1} and {num2} is: {gcd(num1,num2)}")
print(f"GCD of {num3} and {num4} is: {gcd(num3,num4)}")
