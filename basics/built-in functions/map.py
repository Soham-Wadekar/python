# map() - Returns an iterator that applies the specified function to every item of the iterable

import numpy as np

num = [1,2,3,4,5,6]
print(list(map(lambda x: x**2,num)))

code = 'secret'
print(list(map(lambda char: chr(ord(char)+np.random.randint(-10,10)),code)))