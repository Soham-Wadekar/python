# 5. Implement a function to check if a given word is a palindrome using conditionals.

word = "aibohphobia"

if word == word[::-1]:
    print(f"{word.capitalize()} is a palindrome")
else:
    print(f"{word.capitalize()} is not a palindrome")