from dataclasses import dataclass

from strism._shape import Line
from strism._shape import Coordinate

__all__ = ["Side"]


@dataclass
class Side(
    Line,
):
    def __init__(
        self,
        a: Coordinate,
        b: Coordinate,
    ):
        super(QuadSide, self).__init__(
            a,
            b,
        )
