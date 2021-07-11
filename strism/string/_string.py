"""

    *String*

  A string is an abstract string with linear geometry.

"""

from typing import Sequence

from strism._abstract import AbstractString

from strism.letter import Letter

__all__ = ["String"]


class String(
    AbstractString,
    Linear,
):
    geometry: StringGeometry
