with open("intermediates/file handling/files/test.txt", "r") as inp, open(
    "intermediates/file handling/files/out.txt", "w"
) as out:
    print("Reading input file data...")
    content = inp.read()
    print("Done!")

    print("Writing to output file...")
    out.write(content)
    print("Done!")
