# 4. Write a program to find the maximum value in a dictionary.

dict1 = {'A': 10, 'B': 23, 'C': 39, 'D': 82, 'E': 2, 'F': 31}
max_key, max_val = '', 0

for key, val in dict1.items():
    if val > max_val:
        max_key = key
        max_val = val

print(f"The maximum value is of the key {max_key} = {max_val}")