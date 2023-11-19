# 3. Create a program to count the occurrences of each character in a string.

string = "HELLO WORLD"
freq = {letter: string.count(letter) for letter in string}

print(f"Frequency of each character: {freq}")