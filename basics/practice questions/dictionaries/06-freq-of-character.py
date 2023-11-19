# 6. Create a program to count the frequency of each character in a string using a dictionary.

string = "HELLO WORLD"
freq = {letter: string.count(letter) for letter in string if letter.isalnum()}

print(f"Frequency count: {freq}")