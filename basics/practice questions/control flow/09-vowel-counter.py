# 9. Implement a function that counts the number of vowels in a given string using a loop.

string = "Hello World, I'm programming in Python."

string = string.lower()
vowel_count = 0

for char in string:
    if char in "aeiou":
        vowel_count += 1

print(f"No. of vowels in the string is {vowel_count}")
