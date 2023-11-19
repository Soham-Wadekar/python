# 2. Write a function to check if a number is prime.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

num1 = 17
num2 = 20

print(f"{num1} is a prime number" if is_prime(num1) else f"{num1} is not a prime number")
print(f"{num2} is a prime number" if is_prime(num2) else f"{num2} is not a prime number")