"""

    *Border-Corner-Smoothing-Radius*

  Border corner smoothing radius.

"""


from abc import ABCMeta

from ._radius import BorderSmoothingRadius

__all__ = [
    "BorderCornerSmoothingRadius",
    "BorderTopLeftSmoothingRadius",
    "BorderTopRightSmoothingRadius",
    "BorderBottomLeftSmoothingRadius",
    "BorderBottomRightSmoothingRadius",
]


class BorderCornerSmoothingRadius(
    BorderSmoothingRadius,
):
    __metaclass__ = ABCMeta


class BorderTopLeftSmoothingRadius(
    BorderCornerSmoothingRadius,
):
    pass


class BorderTopRightSmoothingRadius(
    BorderCornerSmoothingRadius,
):
    pass


class BorderBottomLeftSmoothingRadius(
    BorderCornerSmoothingRadius,
):
    pass


class BorderBottomRightSmoothingRadius(
    BorderCornerSmoothingRadius,
):
    pass
