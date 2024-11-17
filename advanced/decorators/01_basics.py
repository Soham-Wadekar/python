def decorator_func(func):
    def wrapper(*args, **kwargs):
        print(f"Wrapper executed this before {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@decorator_func
def display():
    print("Display function ran!")


@decorator_func
def display_info(name, age):
    print(f"{name} is {age} years old.")


display()
display_info("Soham", 21)
