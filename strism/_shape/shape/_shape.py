from abc import ABCMeta

from ..coordinate import Coordinate
from ..pixel import Pixel


__all__ = ["Shape"]


class Shape(
    Coordinate,
):
    __metaclass__ = ABCMeta

    radius: Pixel
