# 6. Create a program to capitalize the first letter of each word in a sentence.

sentence = "Lorem ipsum dolor sit amet consectetur, adipisicing elit"

capitalized = " ".join(word.capitalize() for word in sentence.split(" "))
print(f"Capitalized sentence: {capitalized}")
