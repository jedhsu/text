"""

    *Quad Top-Left Corner*

"""

from strism._geoshape import Pixel

from ._corner import QuadCorner

__all__ = ["QuadTopLeftCorner"]


class QuadTopLeftCorner(
    QuadCorner,
):
    def __init__(
        self,
        x: Pixel,
        y: Pixel,
    ):
        super(QuadTopLeftCorner, self).__init__(
            x,
            y,
        )
