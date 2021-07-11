from ..pixel import Pixel


class TestPixel:
    def test_instantiate(self):
        px = Pixel(1)
        assert isinstance(px, Pixel)
        assert isinstance(px, int)
