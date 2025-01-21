# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """
        Method to calculate the area of a shape.
        Should be overridden by derived classes.
        """
        raise NotImplementedError("The area method must be overridden in derived classes.")


class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Initialize a Rectangle with length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate the area of a rectangle.
        Formula: length × width
        """
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """
        Initialize a Circle with radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of a circle.
        Formula: π × radius²
        """
        return math.pi * (self.radius ** 2)

