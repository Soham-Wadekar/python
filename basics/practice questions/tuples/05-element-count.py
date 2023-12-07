# 5. Implement a function to count the occurrences of all the elements in a tuple and store them in a dictionary.

tup = (23, 5, 23, 5, 3, 3, 6, 8, 867, 92, 34, 54, 92, 92)
counts = {}

for num in tup:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

print(f"The counts of all the elements is: {counts}")

# ONE LINE

print("The counts of all the elements is:", {num: tup.count(num) for num in set(tup)})
