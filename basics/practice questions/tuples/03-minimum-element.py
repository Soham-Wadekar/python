# 3. Create a function to find the minimum element in a tuple.

tup = (23,5,23,5,3,3,6,8,867,92,34,54)
min_element = float('inf')

for num in tup:
    if num < min_element:
        min_element = num

print(f"The minimum element of the tuple is {min_element}")

# ONE LINE

tup = (23,5,23,5,3,3,6,8,867,92,34,54)
print(f"The minimum element of the tuple is {sorted(tup)[0]}")