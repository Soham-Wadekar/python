with open('intermediates/file handling/files/test_2.txt','x') as file:
    print("File test_2.txt Created")

try:
    f = open('intermediates/file handling/files/test.txt','x')
    print("File Created")
except FileExistsError as e:
    print("File test.txt already exists")
    print(e)