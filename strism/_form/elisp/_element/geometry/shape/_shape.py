"""

    Element Shape

  The width and height of an element.

"""

from dataclasses import dataclass

from .height import ElementHeight
from .width import ElementWidth

__all__ = [
    "ElementShape",
]


@dataclass
class ElementShape:
    width: ElementWidth
    height: ElementHeight
