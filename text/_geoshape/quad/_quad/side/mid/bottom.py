"""

    *Quad Bottom Midpoint*

"""

from strism._geoshape import Pixel

from ._midpoint import QuadSideMidpoint

__all__ = ["QuadBottomMidpoint"]


class QuadBottomMidpoint(
    QuadSideMidpoint,
):
    def __init__(
        self,
        x: Pixel,
        y: Pixel,
    ):
        super(QuadBottomMidpoint, self).__init__(
            x,
            y,
        )
