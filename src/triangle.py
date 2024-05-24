from src.shape import Shape
from math import sqrt


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("The sides must be positive integers")
        if not (side_a + side_b >= side_c and side_b + side_c >= side_a and side_c + side_a >= side_b):
            raise ValueError("Triangle given sides are not valid")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        super().__init__()

    def get_perimeter(self):
        get_perimeter = self.side_a + self.side_b + self.side_c
        return get_perimeter

    def get_area(self):
        s = self.get_perimeter() / 2
        area = sqrt(s * (s - self.side_c) * (s - self.side_b) * (s - self.side_a))
        return area

