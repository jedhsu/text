"""

    Element Geometry

  The geometry of an element.

"""

from dataclasses import dataclass

from .location import ElementLocation
from .location.coordinate import XCoordinate
from .location.coordinate import YCoordinate

from .shape import ElementShape
from .shape import ElementHeight
from .shape import ElementWidth

__all__ = [
    "ElementGeometry",
]


@dataclass
class ElementGeometry:
    location: ElementLocation
    shape: ElementShape

    @classmethod
    def from_xywh(
        cls,
        x: XCoordinate,
        y: YCoordinate,
        width: ElementWidth,
        height: ElementHeight,
    ):
        return cls(
            ElementLocation.create(
                x,
                y,
            ),
            ElementShape(
                width,
                height,
            ),
        )
