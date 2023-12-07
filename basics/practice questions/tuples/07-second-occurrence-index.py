# 7. Write a program to find the index of the second occurrence of an element in a tuple.

tup = (23, 5, 23, 5, 3, 3, 6, 8, 867, 92, 34, 54, 92, 92)
num = 40

try:
    second_idx = {num: [i for i, number in enumerate(tup) if number == num]}[num][1]
    print(f"The second occurrence of the number {num} is at index {second_idx}")
except:
    print(f"The number {num} does not occur twice in the tuple")
