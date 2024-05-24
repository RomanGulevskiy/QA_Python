import pytest
from src.rectangle import Rectangle
from src.circle import Circle
from src.square import Square
from src.triangle import Triangle


@pytest.mark.parametrize(("side", "area"),
                         [
                             (10, 100),
                             (20, 400),
                             (30, 900)
                         ])
def test_square_area(side, area):
    s = Square(side)
    assert s.get_area() == area, f"The area must be {area}"


@pytest.mark.parametrize(("side", "perimeter"),
                         [
                             (10, 40),
                             (20, 80),
                             (30, 120)
                         ])
def test_square_perimeter(side, perimeter):
    s = Square(side)
    assert s.get_perimeter() == perimeter, f"The perimeter must be {perimeter}"


@pytest.mark.parametrize(("side_a", "side_b", "area"),
                         [
                             (10, 20, 200),
                             (20, 30, 600),
                             (30, 40, 1200)
                         ])
def test_rectangle_area(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area() == area, f"The area must be {area}"


@pytest.mark.parametrize(("side_a", "side_b", "perimeter"),
                         [
                             (10, 20, 60),
                             (20, 30, 100),
                             (30, 40, 140)
                         ])
def test_rectangle_perimeter(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.get_perimeter() == perimeter, f"The perimeter must be {perimeter}"


@pytest.mark.parametrize(("radius", "area"),
                         [
                             (10, 314.1592653589793),
                             (20, 1256.6370614359173),
                             (30, 2827.4333882308138)
                         ])
def test_circle_area(radius, area):
    c = Circle(radius)
    assert c.get_area() == area, f"The area must be {area}"


@pytest.mark.parametrize(("radius", "perimeter"),
                         [
                             (10, 62.83185307179586),
                             (20, 125.66370614359172),
                             (30, 188.49555921538757)
                         ])
def test_circle_perimeter(radius, perimeter):
    c = Circle(radius)
    assert c.get_perimeter() == perimeter, f"The perimeter must be {perimeter}"


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area"),
                         [
                             (20, 20, 30, 198.4313483298443),
                             (30, 30, 40, 447.21359549995793),
                             (40, 40, 50, 780.6247497997998)
                         ])
def test_triangle_area(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_area() == area, f"The area must be {area}"


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "perimeter"),
                         [
                             (10, 20, 30, 60),
                             (20, 30, 40, 90),
                             (30, 40, 50, 120)
                         ],
                         ids=["int", "int", "int"])
def test_triangle_perimeter(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimeter() == perimeter, f"The perimeter must be {perimeter}"