from src.shape import Shape
from math import pi


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("The radius must be a positive integer")
        self.radius = radius
        super().__init__()

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius

