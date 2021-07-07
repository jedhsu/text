"""

    *String*

  A string is an abstract string with geometry.

"""

from typing import Sequence

from strism._abstract import AbstractString

from ..character import Character

__all__ = ["String"]


class String(
    AbstractString,
):
    geometry: StringGeometry
