# 2. Implement a program to remove common elements from two sets.

setA = {1,2,3,4,5,6}
setB = {4,5,6,7,8,9}

print(f"After removing common elements\nSet A: {setA.difference(setB)} \t Set B: {setB.difference(setA)}")