# 8. Implement a program to add elements to a set and update its values.

setA = {1, 2, 3, 4, 5, 6}
elem_to_be_added = [7, 8, 9, 10]

for elem in elem_to_be_added:
    setA.add(elem)

print(f"The set after adding new elements is: {setA}")
