nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(num):
    if num % 2 == 0:
        return True
    return False


even_nums = filter(is_even, nums)
print(list(even_nums))
