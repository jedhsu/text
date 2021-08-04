from ..height import ElementHeight


class TestHeight:
    def test_instantiate(self):
        height = ElementHeight(10)
        assert isinstance(height, ElementHeight)
        assert isinstance(height, int)
        assert height == 10
