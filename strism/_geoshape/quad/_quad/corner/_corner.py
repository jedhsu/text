"""

    *Quad Corner*

  The corner of a quad.

"""

from abc import ABCMeta

from strism._geoshape.point import Point

__all__ = ["QuadCorner"]


class QuadCorner(
    Point,
):
    __metaclass__ = ABCMeta
