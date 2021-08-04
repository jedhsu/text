from ..ypos import Pixel
from ..ypos import Coordinate

from ..ypos import ElementYpos


class TestElementYpos:
    def test_init(self):
        var = ElementYpos(5)
        assert isinstance(var, ElementYpos)
        assert isinstance(var, Pixel)
        assert isinstance(var, Coordinate)
