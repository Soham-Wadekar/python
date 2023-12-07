# 9. Write a program to check if all values in a dictionary are unique.

dict1 = {"A": 432, "B": 882, "C": 329, "D": 412, "E": 736, "F": 201}
unique_vals = []

for val in dict1.values():
    if val not in unique_vals:
        unique_vals.append(val)

if len(unique_vals) == len(dict1):
    print("All values are unique")
else:
    print("Some values are repeated")

# Method 2

if len(set(dict1.values())) == len(dict1.values()):
    print("All values are unique")
else:
    print("Some values are repeated")
