# 6. Create a program to check if a given element exists in a tuple and store all its indices inside a list as value of a dictionary.

tup = (23, 5, 23, 5, 3, 3, 6, 8, 867, 92, 34, 54, 92, 92)
num_to_be_checked = 92
idxs = {num_to_be_checked: []}

for i in range(len(tup)):
    if tup[i] == num_to_be_checked:
        idxs[num_to_be_checked].append(i)

if idxs[num_to_be_checked] == []:
    print(f"Element {num_to_be_checked} does not exist in the dictionary")
else:
    print(
        f"The element {num_to_be_checked} exists at index(ices): {idxs[num_to_be_checked]}"
    )

# Method 2

tup = (23, 5, 23, 5, 3, 3, 6, 8, 867, 92, 34, 54, 92, 92)
num_to_be_checked = 92

idxs = {num_to_be_checked: [i for i, num in enumerate(tup) if num == num_to_be_checked]}

if idxs[num_to_be_checked] == []:
    print(f"Element {num_to_be_checked} does not exist in the dictionary")
else:
    print(
        f"The element {num_to_be_checked} exists at index(ices): {idxs[num_to_be_checked]}"
    )
