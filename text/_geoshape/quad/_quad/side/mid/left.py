"""

    *Quad Left Midpoint*

"""

from strism._geoshape import Pixel

from ._midpoint import QuadSideMidpoint

__all__ = ["QuadLeftMidpoint"]


class QuadLeftMidpoint(
    QuadSideMidpoint,
):
    def __init__(
        self,
        x: Pixel,
        y: Pixel,
    ):
        super(QuadLeftMidpoint, self).__init__(
            x,
            y,
        )
