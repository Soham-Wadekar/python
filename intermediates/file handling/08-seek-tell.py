# seek(offset, whence): Moves the file pointer to a specified position. The offset parameter indicates the number of bytes to move, and whence specifies the reference point (0 for the beginning of the file, 1 for the current position, and 2 for the end).

# tell(): Returns the current position of the file pointer.

with open("intermediates/file handling/files/test.txt", "r") as f:
    content = f.read(10)
    position = f.tell()

    print(f"Content: {content}\nPosition: {position}")

    f.seek(5, 0)
    new_pos = f.tell()
    print(f"New Position: {new_pos}")
