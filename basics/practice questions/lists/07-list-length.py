# 7. Write a program to sort a list of strings based on their length.

lst = ["apple", "banana", "pomegranate", "guava", "pineapple", "fig"]
by_len = sorted(lst, key=len)
print(f"Sorted List by Length of String is: {by_len}")

## ONE LINE

by_len = sorted(
    ["apple", "banana", "pomegranate", "guava", "pineapple", "fig"], key=len
)
print(f"Sorted List by Length of String is: {by_len}")
