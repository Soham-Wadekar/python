# 1. Write a program to check if a key exists in a dictionary.

dict1 = {'A': 1, 'B': 5, 'C': 3}
key = 'A'

if key in dict1.keys():
    print(f"Key {key} Found!")
else:
    print("Key not in the dictionary")