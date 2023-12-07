# 10. Write a program to rotate a list to the left by a specified number of positions.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n_pos = 3

for _ in range(n_pos):
    num = lst.pop(0)
    lst.append(num)

print(f"List after rotating {n_pos} positions to the left is: {lst}")

# Method 2

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n_pos = 3

lst = lst[n_pos:] + lst[:n_pos]
print(f"List after rotating {n_pos} positions to the left is: {lst}")

## ONE LINE

print(
    f"List after rotating 3 positions to the left is: {[1,2,3,4,5,6,7,8,9][3:]+[1,2,3,4,5,6,7,8,9][:3]}"
)
