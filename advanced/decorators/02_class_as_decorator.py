class DecoratorClass(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Call method executed this before {self.func.__name__}")
        return self.func(*args, **kwargs)


@DecoratorClass
def display():
    print("Display function ran!")


@DecoratorClass
def display_info(name, age):
    print(f"{name} is {age} years old.")


display()
display_info("Soham", 21)
