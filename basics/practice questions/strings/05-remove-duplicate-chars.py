# 5. Implement a program to remove duplicate characters from a string.

string = "HELLO WORLD"

unique_chars = "".join(char for char in string if string.count(char)==1)

print(f"The string without repeating characters is: {unique_chars}")