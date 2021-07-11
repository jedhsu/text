"""

    *Quad Top-Side*

  The top side of a quad.

"""

from dataclasses import dataclass

from strism._geoshape import Point

from ._side import QuadSide

__all__ = ["QuadTopSide"]


@dataclass
class QuadTopSide(
    QuadSide,
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
