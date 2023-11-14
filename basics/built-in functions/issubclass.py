# issubclass() - Returns True if class is a subclass

class A:
    pass

class B(A):
    pass

print(issubclass(B,A))
print(issubclass(A,B))