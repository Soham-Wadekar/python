# open() - Opens a file and returns a stream

"""
MODES
'r' - Open for reading (default)
'w' - Open for writing, truncating the file first
'x' - Open for exclusive creation, failing if the file already exists
'a' - Open for writing, appends to the end of the file if it already exists
'b' - Binary mode
't' - Text mode (default)
'+' - Open for updating (reading and writing)
"""

f = open("basics/built-in functions/abs.py", "r")
lines = f.readlines()
print(lines)
f.close()

with open("basics/built-in functions/int.py", "r") as f:
    print(f.readlines())
