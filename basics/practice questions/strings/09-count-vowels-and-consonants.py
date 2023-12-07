# 9. Write a program to count the number of vowels and consonants in a string.

string = "lorem ipsum dolor sit amet consectetur, adipisicing elit"
string = string.lower()

vowel_count = sum(1 for letter in string if letter in "aeiou")
consonant_count = sum(
    1 for letter in string if letter.isalpha() and letter not in "aeiou"
)

print(f"No. of vowels: {vowel_count}\nNo. of consonants: {consonant_count}")
