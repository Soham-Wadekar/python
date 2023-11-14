# zip() - Iterates over several iterables in parallel, producing tuples with an items from each one

str1 = "Hello"
vals = list(range(5))
print(zip(str1,vals))
print(list(zip(str1,vals)))

print(list(zip("hello",range(10),range(3)))) # Continues iterating till one iterator ends