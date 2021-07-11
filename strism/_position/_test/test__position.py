from .._position import ElementXpos
from .._position import ElementYpos

from .._position import ElementPosition


class TestElementPosition:
    def test_init(self):
        var = ElementPosition(
            ElementXpos(5),
            ElementYpos(10),
        )
        assert isinstance(var, ElementPosition)
        assert var.x == ElementXpos(5)
        assert var.y == ElementYpos(10)

    def test_create(self):
        var = ElementPosition.create(5, 10)
        assert isinstance(var, ElementPosition)
        assert var.x == ElementXpos(5)
        assert var.y == ElementYpos(10)
