from ..point import Pixel
from ..point import Point


class TestPoint:
    def test_instantiate(self):
        pt = Point(
            Pixel(1),
            Pixel(2),
        )
        assert isinstance(pt, Point)
        assert pt.x == Pixel(1)
        assert pt.y == Pixel(2)

    def test_create(self):
        pt = Point.create(1, 2)
        assert isinstance(pt, Point)
        assert pt.x == Pixel(1)
        assert pt.y == Pixel(2)

    def test_repr(self):
        pt = Point.create(1, 2)
        assert repr(pt) == "(1, 2)"

    def test_add(self):
        pt1 = Point.create(1, 2)
        pt2 = Point.create(3, 4)
        assert pt1 + pt2 == Point.create(4, 6)

    def test_sub(self):
        pt1 = Point.create(1, 2)
        pt2 = Point.create(3, 4)
        assert pt1 - pt2 == Point.create(-2, -2)
