# 5. Create a program that attempts to access a key in a dictionary, handling the KeyError if the key is not present.

dict1 = {'A': 1, 'B': 3, 'C': 8}
key = 'D'

try:
    print(f"Value at {key} = {dict1[key]}")
except KeyError:
    print("Key does not exist in the dictionary")