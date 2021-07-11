"""

    *Quad Top Midpoint*

"""

from strism._geoshape import Pixel

from ._midpoint import QuadSideMidpoint

__all__ = ["QuadTopMidpoint"]


class QuadTopMidpoint(
    QuadSideMidpoint,
):
    def __init__(
        self,
        x: Pixel,
        y: Pixel,
    ):
        super(QuadTopMidpoint, self).__init__(
            x,
            y,
        )
