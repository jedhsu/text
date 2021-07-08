from dataclasses import dataclass

from ..coordinate import Coordinate

__all__ = ["Line"]


@dataclass
class Line:
    a: Coordinate
    b: Coordinate

    @property
    def length(self):
        pass
