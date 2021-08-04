"""

    *Quad Top-Right Corner*

"""

from strism._geoshape import Pixel

from ._corner import QuadCorner

__all__ = ["QuadTopRightCorner"]


class QuadTopRightCorner(
    QuadCorner,
):
    def __init__(
        self,
        x: Pixel,
        y: Pixel,
    ):
        super(QuadTopRightCorner, self).__init__(
            x,
            y,
        )
