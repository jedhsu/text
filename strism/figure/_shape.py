"""

    *Figure*

"""

from abc import ABCMeta

from ..point import Point
from ..pixel import Pixel


__all__ = ["Shape"]


class Shape(
    Coordinate,
):
    __metaclass__ = ABCMeta

    radius: Pixel
