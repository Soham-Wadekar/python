"""
Abstract classes in Python are classes which cannot be instantiated.
The method of these classes are called abstract methods.
They are used so as to define the blueprints for other subclasses
"""

from abc import ABC, abstractmethod
import numpy as np


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(np.pi * self.radius**2, 3)

    def perimeter(self):
        return round(2 * np.pi * self.radius)


class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return round(self.base * self.height, 3)

    def perimeter(self):
        return round(2 * (self.base + self.height), 3)


try:
    shp = Shape()
except:
    print("Class Shape is an abstract class and cannot be instantiated")

cir = Circle(10)
print(cir.area())
print(cir.perimeter())

rect = Rectangle(10, 20)
print(rect.area())
print(rect.perimeter())
