# 8. Implement a program to create a dictionary from two lists.

keys = list('ABCDEF')
values = [432,882,329,412,736,201]

new_dict = dict(zip(keys,values))
print(f"The dictionary from the two lists {keys} and {values} is:\n{new_dict}")