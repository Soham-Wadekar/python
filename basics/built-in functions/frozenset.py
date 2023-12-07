# frozenset() - Returns an immutable version of a set

lst = [1, 2, 3, 4]
s = set(lst)
s.add(5)

print(s)

fs = frozenset(lst)
print(fs)
