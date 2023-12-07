# 3. Write a function that attempts to access an element at an index in a list, handling the IndexError gracefully.


def access_list(lst, idx):
    try:
        print(f"The element at index {idx} is {lst[idx]}")
    except IndexError:
        print("List index out of range")


access_list([1, 2, 3], 2)
access_list([1, 2], 5)
