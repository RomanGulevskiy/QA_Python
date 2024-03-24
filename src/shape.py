from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, shape):
        if not isinstance(Shape, shape):
            raise ValueError("Wrong object! A shape object is expected.")
        return self.get_area() + shape.get_area()
