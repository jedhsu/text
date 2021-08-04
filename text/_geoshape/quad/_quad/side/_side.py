"""

    *Quad Side*

  A side of a quad.

"""

from dataclasses import dataclass

from strism._geoshape import Line
from strism._geoshape import Point

__all__ = ["QuadSide"]


@dataclass
class QuadSide(
    Line,
):
    def __init__(
        self,
        a: Point,
        b: Point,
    ):
        super(QuadSide, self).__init__(
            a,
            b,
        )
