import math

def area_of_rectangle(length, breadth):
    '''Calculates area of rectangle'''
    return length * breadth

def area_of_circle(radius, roundoff=2):
    '''Calculates area of circle'''
    return round(math.pi * radius ** 2, roundoff) 
