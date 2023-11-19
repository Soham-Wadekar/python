# 2. Implement a program to check if a string is a palindrome.

string = "aibohphobia"
print(f"String '{string}' is a Palindrome" if string==string[::-1] else f"String '{string}' is not a palindrome")