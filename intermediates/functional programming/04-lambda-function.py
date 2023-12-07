# METHOD 1
add = lambda x, y: x + y
print(add(1, 3))
print("===" * 5)

# METHOD 2
print((lambda x, y: x + y)(15, 10))
print("===" * 5)

# METHOD 3
product = lambda x, y=3, z=5: x * y * z
print(product(2))
print(product(2, 4))
print("===" * 5)

# METHOD 4
add = lambda *nums: sum(nums)
print(add(10, 12))
print(add(1, 2, 3, 4, 5))
print(add(100))
print("===" * 5)

# METHOD 5
higher_ord_func = lambda x, func: x * func(x)
print(higher_ord_func(10, lambda x: 3 * x))
print("===" * 5)

# METHOD 6
print((lambda x: (x % 2 and "odd" or "even"))(15))
