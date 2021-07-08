from abc import ABCMeta

from strism._shape import Point

__all__ = ["Midpoint"]


class Midpoint(
    Point,
):
    __metaclass__ = ABCMeta
