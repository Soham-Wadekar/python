def gen(n):
    for i in range(n):
        yield i             # Returns the value immediately by pausing the function

for i in gen(5):
    print(i)