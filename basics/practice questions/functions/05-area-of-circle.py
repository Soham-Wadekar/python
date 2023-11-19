# 5. Write a program with a function that calculates the area of a circle given its radius.
import math

def area_of_circle(r):
    return round(math.pi * r * r, 2)

radius = 3
print(f"Area of the circle with {radius} is {area_of_circle(radius)} sq. units")