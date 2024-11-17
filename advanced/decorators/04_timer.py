import time


def timer_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} executed in {end - start} seconds")

    return wrapper


class TimerClass(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        self.func(*args, **kwargs)
        end = time.time()
        print(f"Function {self.func.__name__} executed in {end - start} seconds")


@timer_func
def test_func_1():
    time.sleep(2)
    print("This is test function 1")


@TimerClass
def test_func_2():
    time.sleep(5)
    print("This is test function 2")


test_func_1()
test_func_2()
