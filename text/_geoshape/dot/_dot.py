"""

    *Dot*

  A shape at a coordinate.

"""

from dataclasses import dataclass

from ..coordinate import Coordinate


@dataclass
class Dot(
    Coordinate,
):
    shape: Shape
