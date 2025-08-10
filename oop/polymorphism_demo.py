"""
This module demonstrates polymorphism with Shape, Rectangle, and Circle classes.
"""
import math

class Shape:
    """
    A base class for geometric shapes.
    """
    def area(self):
        """
        Calculates the area of the shape. This method is meant to be
        overridden by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method.")

class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.

    Attributes:
        length (float or int): The length of the rectangle.
        width (float or int): The width of the rectangle.
    """
    def __init__(self, length, width):
        """Initializes the Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float or int: The area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """
    A class representing a circle, inheriting from Shape.

    Attributes:
        radius (float or int): The radius of the circle.
    """
    def __init__(self, radius):
        """Initializes the Circle with a radius."""
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)