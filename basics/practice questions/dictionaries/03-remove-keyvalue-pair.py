# 3. Create a function to remove a key-value pair from a dictionary.

def remove_kv_pair(dictionary,key):
    del dictionary[key]
    return dictionary

dict1 = {'A': 10, 'B': 23, 'C': 39, 'D': 82}
key_to_be_removed = 'C'
new_dict = remove_kv_pair(dict1,key=key_to_be_removed)
print(f"The dictionary after removing the key {key_to_be_removed} is {new_dict}")