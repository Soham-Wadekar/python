# 10. Write a program to update the values of specific keys in a dictionary.

dict1 = {'A': 432, 'B': 882, 'C': 329, 'D': 412, 'E': 736, 'F': 201}
key = 'C'
val = 123

dict1.update({key:val})
print(f"Update Dictionary: {dict1}")