# 7. Write a program to check if two sets are disjoint.

setA = {1, 2, 3, 4, 5, 6}
setB = {4, 5, 6, 7, 8, 9}

setC = {1, 2, 3}
setD = {4, 5, 6}

print(
    f"Set A {setA} and Set B {setB} are Disjoint Sets"
    if setA.isdisjoint(setB)
    else f"Set A {setA} and Set B {setB} are Joint Sets"
)
print(
    f"Set C {setC} and set D {setD} are Disjoint Sets"
    if setC.isdisjoint(setD)
    else f"Set C {setC} and set D {setD} are Joint Sets"
)
