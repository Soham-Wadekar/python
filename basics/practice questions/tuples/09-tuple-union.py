# 9. Write a program to find the union of two tuples.

tup1 = (1, 2, 3, 4, 5, 6)
tup2 = (4, 5, 6, 7, 8, 9)

print(f"The union of the tuple {tup1} and {tup2} is: {tuple(set(tup1+tup2))}")
