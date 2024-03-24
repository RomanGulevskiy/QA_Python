from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("The side must be a positive integer")
        super().__init__(side_a, side_a)

