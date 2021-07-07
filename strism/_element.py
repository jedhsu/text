"""

    *Element*

  An element is an abstract element residing in space.

  This imbues the element with a *geometry*.

"""

from strism._abstract import AbstractElement
from strism._geometry import Geometry

__all__ = ["AbstractElement"]


class Element(
    AbstractElement,
):
    geometry: Geometry
