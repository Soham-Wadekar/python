# all() - Returns True if all elements of the iterable are true (of if the iterable is empty)

a = [1, 0, 1, 2, 5]
print(all(a))

b = [True, True, 1, 2, ""]
print(all(b))

c = [[1, 2], [False]]
print(all(c))

d = [[0, 0], [0, 0], [0, 0]]
print(all(d))

e = [[], True, [1]]
print(all(e))
