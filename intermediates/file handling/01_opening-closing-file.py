# To open any file, we can use the open() function. There are two ways to open a file

# METHOD 1
f = open('intermediates/file handling/files/test.txt')
print(f"The variable f is of type {type(f)}")

# METHOD 2
with open('intermediates/file handling/files/test.txt','r') as f:
    print(f"The variable f is of type {type(f)}")


'''
FILE OPENING MODES
'r' - Open for reading (default)
'w' - Open for writing, truncating the file first
'x' - Open for exclusive creation, failing if the file already exists
'a' - Open for writing, appends to the end of the file if it already exists
'b' - Binary mode
't' - Text mode (default)
'+' - Open for updating (reading and writing)
'''

# Closing the file

f.close()