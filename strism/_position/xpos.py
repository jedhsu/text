"""

    *Element X-Pos*

  The element's x-position.

"""

from strism._geoshape import Pixel

from ._coordinate import Coordinate

__all__ = ["ElementXpos"]


class ElementXpos(
    Pixel,
    Coordinate,
):
    def __init__(
        self,
        height: int,
    ):
        super(ElementXpos, self).__init__(
            height,
        )
