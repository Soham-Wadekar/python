# 3. Create a program with a function that generates Fibonacci sequence up to a specified term.

def fibonacci(n):
    series = [0, 1]
    for _ in range(2,n):
        next_term = series[-1] + series[-2]
        series.append(next_term)

    return series

print(fibonacci(10))