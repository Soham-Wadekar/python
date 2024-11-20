'''
Functools.wraps preserves the metadata of the original function
'''
from functools import wraps

def decorator_without_wraps(func):

    def wrapper(*args, **kwargs):
        '''Wrapper (without wraps) docstring'''
        return func(*args, **kwargs)
    return wrapper

def decorator_with_wraps(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        '''Wrapper (with wraps) docstring '''
        return func(*args, **kwargs)
    return wrapper

@decorator_without_wraps
def hello_1(name):
    '''First hello'''
    print(f"Hello {name}")

@decorator_with_wraps
def hello_2(name):
    '''Second hello'''
    print(f"Hello again {name}")

hello_1("Soham")
print(hello_1.__name__)
print(hello_1.__doc__)
print()
hello_2("Soham")
print(hello_2.__name__)
print(hello_2.__doc__)