"""

    *Quad Bottom-Right Corner*

"""

from strism._geoshape import Pixel

from ._corner import QuadCorner

__all__ = ["QuadBottomRightCorner"]


class QuadBottomRightCorner(
    QuadCorner,
):
    def __init__(
        self,
        x: Pixel,
        y: Pixel,
    ):
        super(QuadBottomRightCorner, self).__init__(
            x,
            y,
        )
