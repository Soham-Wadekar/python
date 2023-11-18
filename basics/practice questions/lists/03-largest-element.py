# 3. Write a program to find the largest element in a list.

lst = [23,5,23,5,3,3,6,8,867,92,34,54]
largest_num = 0

for num in lst:
    if num > largest_num:
        largest_num = num

print(f"The largest number in the list is {largest_num}")

# Method 2

lst = [23,5,23,5,3,3,6,8,867,92,34,54]
print(f"The largest number in the list is {sorted(lst,reverse=True)[0]}")

## ONE LINE

print(f"The largest number in the list is {sorted([23,5,23,5,3,3,6,8,867,92,34,54],reverse=True)[0]}")