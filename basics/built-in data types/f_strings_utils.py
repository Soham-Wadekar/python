'''File with all variables and other utilities'''

from datetime import datetime

class Text:
    def __init__(self, text):
        self.text = text

    def __format__(self, format_spec):
        match format_spec:
            case "": return self.text
            case "shout": return self.text.upper() + '!!'
            case "whisper": return self.text.lower() + '...'
            case "count": return str(len(self.text))
            case _: raise ValueError(f"Wrong format specifier!!")

bin_num = 0b100
big_num = 1000000000
char = 'c'
date = datetime.now()
float_num = 93.82736474839
hex_num = 0xff
inf = float('inf')
name = "Python"
num = 192
oct_num = 0o10
percent = .5392
small_num = 9
text = Text("hello world")