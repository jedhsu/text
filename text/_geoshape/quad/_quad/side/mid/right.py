"""

    *Quad Right Midpoint*

"""

from strism._geoshape import Pixel

from ._midpoint import QuadSideMidpoint

__all__ = ["QuadRightMidpoint"]


class QuadRightMidpoint(
    QuadSideMidpoint,
):
    def __init__(
        self,
        x: Pixel,
        y: Pixel,
    ):
        super(QuadRightMidpoint, self).__init__(
            x,
            y,
        )
