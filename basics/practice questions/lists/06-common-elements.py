# 6. Create a program to find common elements between two lists.

lst1 = [32, 98, 6, 38, 42, 332, 28, 432, 87, 92, 2]
lst2 = [2, 6, 328, 28, 239, 210, 2132, 92]

common_elements = []

for num in lst1:
    if num in lst2 and num not in common_elements:
        common_elements.append(num)

print(f"The common elements from both the lists are: {sorted(common_elements)}")

## ONE LINE

print(
    f"The common elements from both the lists are: {sorted(list(set([32, 98, 6, 38, 42, 332, 28, 432, 87, 92, 2]).intersection(set([2, 6, 328, 28, 239, 210, 2132, 92]))))}"
)
