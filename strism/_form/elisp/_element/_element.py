"""

    *Element*

  Editor physical element.

"""

from abc import ABCMeta
from dataclasses import dataclass

from .geometry import ElementGeometry

from .geometry import ElementLocation
from .geometry import XCoordinate
from .geometry import YCoordinate

from .geometry import ElementShape
from .geometry import ElementWidth
from .geometry import ElementHeight

__all__ = ["Element"]


@dataclass
class Element:
    __metaclass__ = ABCMeta

    geometry: ElementGeometry

    @classmethod
    def from_xywh(
        cls,
        x: XCoordinate,
        y: YCoordinate,
        width: ElementWidth,
        height: ElementHeight,
    ):
        return cls(
            ElementGeometry(
                ElementLocation.create(
                    x,
                    y,
                ),
                ElementShape(
                    width,
                    height,
                ),
            ),
        )
