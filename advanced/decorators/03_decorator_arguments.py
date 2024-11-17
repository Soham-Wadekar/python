def repeat_func(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


class RepeatClass(object):

    def __init__(self, times):
        self.times = times

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                func(*args, **kwargs)

        return wrapper


@repeat_func(2)
def hello():
    print("Hello!")


@RepeatClass(3)
def bye():
    print("Bye!", end=" ")


hello()
bye()
