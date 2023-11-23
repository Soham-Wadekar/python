import os

with open('intermediates/file handling/files/delete.txt','x') as f:
    print("File Created")

if os.path.exists('intermediates/file handling/files/delete.txt'):
    print("Deleting File...")
    os.remove('intermediates/file handling/files/delete.txt')
    print("Done!")
else:
    print("The file does not exist.")