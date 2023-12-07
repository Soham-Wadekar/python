# filter() - Constructs an iterator from the elements of the iterable for which the function returns True


def func(val):
    return val % 2 == 0


nums = list(range(10))
even = filter(func, nums)

print(list(even))
