# 5. Implement a program to sort a dictionary by its values.

dict1 = {'A': 10, 'B': 23, 'C': 39, 'D': 82, 'E': 2, 'F': 31}

sorted_dict = dict(sorted(dict1.items(), key=lambda item: item[1]))
print(f"Sorted Dictionary is: {sorted_dict}")