def mean(numbers):
    '''Calculations the arithmetic mean of the numbers'''
    return sum(numbers) / len(numbers)

def median(numbers):
    '''Calculations the median of the numbers'''
    sorted_nums = sorted(numbers)

    if len(numbers) % 2 == 0:
        med1 = sorted_nums[len(numbers) // 2]
        med2 = sorted_nums[len(numbers) // 2 - 1]
        med = (med1 + med2) / 2
    else:
        med = sorted_nums[len(numbers) // 2]
    return med
