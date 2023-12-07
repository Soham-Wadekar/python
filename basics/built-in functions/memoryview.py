# memoryview() - Returns a "memoryview" object created from a given argument

x = b"abcdef"
mem = memoryview(x)

print(list(mem))  # Returns ASCII value of each byte

print(bytes(mem[1:4]))
