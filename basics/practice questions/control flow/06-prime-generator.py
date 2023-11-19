# 6. Write a program that generates a list of prime numbers within a specified range.

primes = []
start = 10
end = 100

for num in range(max(2,start),end + 1):
    is_prime = True

    for i in range(2,int(num*0.5)+1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)

print(f"The primes between {start} and {end} are: {primes}")