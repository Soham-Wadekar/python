# 7. Implement a program with a function that checks if a given year is a leap year.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

year = 2000
print(f"{year} is a leap year" if is_leap_year(year) else f"{year} is not a leap year")