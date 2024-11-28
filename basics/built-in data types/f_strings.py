'''All about f-strings'''

from f_strings_utils import *

# Basic f-string
print(f"Name: {name}, Num: {num}\n")
print(f"{inf:F}")

# Quick Debugging with f-strings
print(f"Name: {name=}")
print(f"{isinstance(name, str)=}\n")

# Rounding numbers
print(f"Rounded Number: {float_num:.2f}")
print(f"Percent Number: {percent:.2%}\n")

# Format big numbers
print(f"Big Number: {big_num:_}")
print(f"Big Number: {big_num:,}\n")

# Alignment
print(f"Left margin | {name:<20} | Right Margin")
print(f"Left margin | {name:_^20} | Right Margin\n")
print(f"Left margin | {name:>20} | Right Margin")

# Different Numbering Systems
print(f"Num: {small_num} [bin: {small_num:b}]")
print(f"Bin: 0b{bin_num:b} [num: {bin_num:d}]\n")
print(f"Num: {small_num} [oct: {small_num:o}]")
print(f"Oct: 0o{oct_num:o} [num: {oct_num:d}]\n")
print(f"Num: {num} [hex: {num:x}]")
print(f"Num: {num} [hex: {num:X}]")
print(f"Hex: 0x{hex_num:x} [num: {hex_num:d}]\n")

# Unicode character conversion
print(f"Char: {num} [Unicode: {num:c}]\n")

# Scientific Notation
print(f"Big Number: {big_num} [S.N.: {big_num:.2e}]")
print(f"Big Number: {big_num} [S.N.: {big_num:E}]\n")

# Datetime formatting
print(f"Today's Date: {date:%x}")
print(f"Today's Full Date: {date:%c}")
print(f"Today's Time: {date:%H:%M:%S}\n")

# Nested f-strings (Pretty unnecessary, actually)
print(f"F-string #1: {1 + 1}, \
      {f"F-string #2: {2 + 2}, \
       {f"F-string #3: {3 + 3}"}"}\n")

# Custom f-strings
print(f"Text: {text} [shout: {text:shout}]")
print(f"Text: {text} [whisper: {text:whisper}]")
print(f"Text: {text} [word_count: {text:count}]")