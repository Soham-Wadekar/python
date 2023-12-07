# 4. Write a program to check if two strings are anagrams.

str1 = "LISTEN"
str2 = "SILENT"

freq1 = {letter: str1.count(letter) for letter in str1}
freq2 = {letter: str2.count(letter) for letter in str2}

print(
    f"Strings '{str1}' and '{str2}' are anagrams"
    if freq1 == freq2
    else f"Strings '{str1}' and '{str2}' are not anagrams"
)
