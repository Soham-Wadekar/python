with open("intermediates/file handling/files/test.txt", "a") as f:
    f.write("\n================= News lines added =================")

with open("intermediates/file handling/files/test.txt", "r") as f:
    print(f.read())
