# 1. Write a Python program that takes a year as input and determines whether it is a leap year or not.

year = 2023

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
