# polymorphism_demo.py

import math

class Shape:
    """Base class for all shapes."""

    def area(self):
        """Method to be overridden by derived classes."""
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    """Rectangle shape, derived from Shape."""

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle: length × width."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape, derived from Shape."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate area of a circle: π × r²."""
        return math.pi * (self.radius ** 2)


# Demo usage
if __name__ == "__main__":
    shapes = [
        Rectangle(5, 3),
        Circle(4),
        Rectangle(10, 2)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area():.2f}")
