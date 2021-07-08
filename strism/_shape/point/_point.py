from dataclasses import dataclass

from ..coordinate import Coordinate


@dataclass
class Point(
    Coordinate,
):
    shape: Shape
