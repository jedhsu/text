"""

    *String*

  A string is an abstract string with geometry.


"""

from typing import Sequence

from ..character import Character

__all__ = ["String"]


class String(AbstractString):
    geometry: StringGeometry
