# 8. Implement a program to flatten a nested list.

lst = [[1, 2, 3], [532, 6, 3], [4, 2], [2], [32, 1, 32, 5, 7, 8, 3]]
flattened_list = []

for sub_list in lst:
    for elem in sub_list:
        flattened_list.append(elem)

print(f"Flattened List: {flattened_list}")

## ONE LINE

print(
    f"Flattened List: {list(elem for sub_list in [[1,2,3],[532,6,3],[4,2],[2],[32,1,32,5,7,8,3]] for elem in sub_list)}"
)
