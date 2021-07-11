"""

    *Figure*

  A figure in space.

"""

from abc import ABCMeta

from ..point import Coordinate
from ..pixel import Pixel


__all__ = ["Shape"]


class Figure(
    Coordinate,
):
    __metaclass__ = ABCMeta

    radius: Pixel
