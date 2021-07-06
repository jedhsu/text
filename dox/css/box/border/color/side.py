"""

    *Border-Side-Color*

  Border side color.

"""


from abc import ABCMeta

from ._color import BorderColor

__all__ = [
    "BorderSideColor",
    "BorderTopColor",
    "BorderRightColor",
    "BorderBottomColor",
    "BorderLeftColor",
]


class BorderSideColor(
    BorderColor,
):
    __metaclass__ = ABCMeta


class BorderTopColor(
    BorderSideColor,
):
    pass


class BorderRightColor(
    BorderSideColor,
):
    pass


class BorderBottomColor(
    BorderSideColor,
):
    pass


class BorderLeftColor(
    BorderSideColor,
):
    pass
