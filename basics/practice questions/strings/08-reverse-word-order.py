# 8. Write a program to reverse the order of words in a sentence.

sentence = "lorem ipsum dolor sit amet consectetur, adipisicing elit"

reverse_sentence = " ".join(word for word in sentence.split(" ")[::-1])
print(reverse_sentence)