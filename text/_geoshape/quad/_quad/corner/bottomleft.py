"""

    *Quad Bottom-Left Corner*

"""

from strism._geoshape import Pixel

from ._corner import QuadCorner

__all__ = ["QuadBottomLeftCorner"]


class QuadBottomLeftCorner(
    QuadCorner,
):
    def __init__(
        self,
        x: Pixel,
        y: Pixel,
    ):
        super(QuadBottomLeftCorner, self).__init__(
            x,
            y,
        )
