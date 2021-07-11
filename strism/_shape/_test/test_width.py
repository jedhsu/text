from ..width import ElementWidth


class TestWidth:
    def test_instantiate(self):
        width = ElementWidth(10)
        assert isinstance(width, ElementWidth)
        assert isinstance(width, int)
        assert width == 10
