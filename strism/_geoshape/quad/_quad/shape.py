"""

    *Quad Shape*

  The shape of a quad.

"""

from dataclasses import dataclass

from strism._geoshape import Pixel
from strism._shape import ElementShape

__all__ = ["QuadShape"]


@dataclass
class QuadShape(
    ElementShape,
):
    def __init__(
        self,
        width: Pixel,
        height: Pixel,
    ):
        super(QuadShape, self).__init__(
            width,
            height,
        )
