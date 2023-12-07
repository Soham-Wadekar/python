# 2. Implement a program to remove duplicate elements from a list.

lst = [23, 5, 23, 5, 3, 3, 6, 8, 867, 92, 34, 54, 92, 92]
uniq_list = []

for num in lst:
    if num not in uniq_list:
        uniq_list.append(num)

print(f"Original List: {lst}")
print(f"List without duplicates: {uniq_list}")

# Method 2

lst = [23, 5, 23, 5, 3, 3, 6, 8, 867, 92, 34, 54, 92, 92]
uniq_list = list(set(lst))

print(f"Original List: {lst}")
print(f"List without duplicates: {uniq_list}")

## ONE LINE

print(f"List without duplicates: {list(set([23,5,23,5,3,3,6,8,867,92,34,54]))}")
