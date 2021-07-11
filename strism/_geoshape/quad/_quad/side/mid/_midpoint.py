"""

    *Quad Side Midpoint*

  The midpoint of a quad side.

"""

from abc import ABCMeta

from strism._geoshape import Point

__all__ = ["QuadSideMidpoint"]


class QuadSideMidpoint(
    Point,
):
    __metaclass__ = ABCMeta
