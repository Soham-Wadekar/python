# 4. Write a program to convert a tuple to a list without type casting.

tup = (23,5,23,5,3,3,6,8,867,92,34,54)
lst = [elem for elem in tup]

print(f"Tuple: {tup} ==> List: {lst}")