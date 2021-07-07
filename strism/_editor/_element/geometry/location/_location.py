"""

    Element Location

  The location of an element.

"""

from dataclasses import dataclass

from .coordinate import XCoordinate
from .coordinate import YCoordinate

from ._anchor import ElementLocationAnchor


@dataclass
class ElementLocation:
    x: XCoordinate
    y: YCoordinate
    anchor: ElementLocationAnchor

    @classmethod
    def create(
        cls,
        x: XCoordinate,
        y: YCoordinate,
        anchor: ElementLocationAnchor = ElementLocationAnchor.TopLeft,
    ):
        return cls(
            x,
            y,
            anchor,
        )
