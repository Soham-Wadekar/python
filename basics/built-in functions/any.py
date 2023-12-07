# any() - Returns True if any element of the iterable are true (of if the iterable is empty)

a = [1, 0, 1, 2, 5]
print(any(a))

b = [True, True, 1, 2, ""]
print(any(b))

c = [[1, 2], [False]]
print(any(c))

d = [[0, 0], [0, 0], [0, 0]]
print(any(d))

e = [[], False, 0]
print(any(e))
