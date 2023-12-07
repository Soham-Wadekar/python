# There are multiple ways for reading a file

# To read the entire file
with open("intermediates/file handling/files/test.txt", "r") as file:
    print("====" * 15)
    print(f"The full file is:\n{file.read()}")
    file.close()

# To print a specific number of characters from the file
with open("intermediates/file handling/files/test.txt", "r") as file:
    num_char = 50
    print("====" * 15)
    print(f"The first {num_char} characters from the file are:\n{file.read(num_char)}")
    file.close()

# To read a single line from the file
with open("intermediates/file handling/files/test.txt", "r") as file:
    print("====" * 15)
    print(f"The first line from the file: {file.readline()}")
    file.close()

# To read all the lines one-by-one using a `for` loop
with open("intermediates/file handling/files/test.txt", "r") as file:
    print("====" * 15)
    for i, line in enumerate(file.readlines()):
        print(f"{i+1}: {line}")
    file.close()
