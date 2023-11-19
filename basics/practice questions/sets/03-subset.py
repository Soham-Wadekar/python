# 3. Write a program to check if a set is a subset of another set.

setA = {1,2,3,4,5,6}
setB = {1,2,3}

print(f"Subset" if setB.issubset(setA) else f"Not a Subset")