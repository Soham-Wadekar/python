class Iter:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1

        if self.current >= self.n:
            raise StopIteration
        
        return self.current

x = Iter(5)

for i in x:
    print(i)

print("==="*5)

# Need to create an iter object of x, else next(x) will not work since self.current would not be defined
itr = iter(x)
print(next(x))