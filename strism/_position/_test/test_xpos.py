from ..xpos import Pixel
from ..xpos import Coordinate

from ..xpos import ElementXpos


class TestElementXpos:
    def test_init(self):
        var = ElementXpos(5)
        assert isinstance(var, ElementXpos)
        assert isinstance(var, Pixel)
        assert isinstance(var, Coordinate)
