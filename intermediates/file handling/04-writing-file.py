with open("intermediates/file handling/files/test_1.txt", "r") as f:
    print("Original File")
    print(f.read())
    f.close()

with open("intermediates/file handling/files/test_1.txt", "w") as f:
    f.write("New lines added to this file and old ones were deleted")
    f.close()

with open("intermediates/file handling/files/test_1.txt", "r") as f:
    print("File after writing")
    print(f.read())
    f.close()
