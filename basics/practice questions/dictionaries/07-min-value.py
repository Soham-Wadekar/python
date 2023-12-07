# 7. Write a program to find keys with the minimum value in a dictionary.

dict1 = {"A": 10, "B": 23, "C": 39, "D": 82, "E": 2, "F": 31}
min_key, min_val = "", float("inf")

for key, val in dict1.items():
    if val < min_val:
        min_key = key
        min_val = val

print(f"The minimum value is of the key {min_key} = {min_val}")
