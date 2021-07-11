"""

    *Element Y-Pos*

  The element's y-position.

"""

from strism._geoshape import Pixel

from ._coordinate import Coordinate

__all__ = ["ElementYpos"]


class ElementYpos(
    Pixel,
    Coordinate,
):
    def __init__(
        self,
        height: int,
    ):
        super(ElementYpos, self).__init__(
            height,
        )
