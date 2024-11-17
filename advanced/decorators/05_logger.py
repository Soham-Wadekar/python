from datetime import datetime


def logger_func(func):
    def wrapper(*args, **kwargs):
        with open("advanced/decorators/log.txt", "a") as file:
            func(*args, **kwargs)
            file.write(
                f"[{datetime.now()}] Executed function: '{func.__name__}' with arguments: {args} and kwargs: {kwargs}\n"
            )

    return wrapper


class LoggerClass(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open("advanced/decorators/log.txt", "a") as file:
            self.func(*args, **kwargs)
            file.write(
                f"[{datetime.now()}] Executed function: '{self.func.__name__}' with arguments: {args} and kwargs: {kwargs}\n"
            )


@logger_func
def display_info(name, age):
    print(f"{name} is {age} years old!")


@LoggerClass
def display(*args, **kwargs):
    print(f"Args: {args}, Kwargs: {kwargs}")


display_info("Soham", 21)
display("John", 54, person=True, height=172)
