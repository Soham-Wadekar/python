# 2. Implement a program that reads content from a file, handles potential file not found errors, and prints the content.

try:
    with open('demo.txt','r') as file:
        content = file.read()
        print(content)
except:
    print("File not found")