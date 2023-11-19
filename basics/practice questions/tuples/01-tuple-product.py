# 1. Write a program to calculate the product of elements in a tuple.

tup = (1,2,3,4,5,6)
prod = 1
for i in tup:
    prod*=i

print(f"The product of the elements in the tuple is {prod}")
