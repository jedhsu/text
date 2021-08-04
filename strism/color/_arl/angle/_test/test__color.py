from .._color import Color
from .._color import Angle


class TestAngle:
    def test_init(self):
        red = Angle(0)
        assert red == 0
        assert isinstance(red, Color)
        green = Angle(1)
        assert green == 1
