# 8. Implement a program to unzip a list of tuples.

tups = [(1,2,3),(4,),(5,6,7,8,9),(10,11)]
lst = [i for tup in tups for i in tup]
print(f"The unzipped tuple is :{lst}")