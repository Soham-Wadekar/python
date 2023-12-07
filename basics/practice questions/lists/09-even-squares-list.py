# 9. Create a list of squares for even numbers in the range 1 to 10 using list comprehension.

nums = list(range(1, 11))
squares = [x**2 for x in nums if x % 2 == 0]
print(f"The squares of the even numbers from 1 to 10 are: {squares}")

## ONE LINE

print(
    f"The squares of the even numbers from 1 to 10 are: {[x**2 for x in range(1,11) if x % 2 == 0]}"
)
