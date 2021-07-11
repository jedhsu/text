from .._shape import Pixel

from .._shape import ElementShape


class TestShape:
    def test_instantiate(self):
        shape = ElementShape(
            Pixel(5),
            Pixel(10),
        )
        assert isinstance(shape, ElementShape)
        assert shape.width == 5
        assert shape.height == 10

    def test_create(self):
        shape = ElementShape.create(5, 10)
        assert isinstance(shape, ElementShape)
        assert shape.width == 5
        assert shape.height == 10
