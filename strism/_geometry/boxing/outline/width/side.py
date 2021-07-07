"""

    *Border-Side-Width*

  Border side width.

"""


from abc import ABCMeta

from ._width import BorderWidth

__all__ = [
    "BorderSideWidth",
    "BorderTopWidth",
    "BorderRightWidth",
    "BorderBottomWidth",
    "BorderLeftWidth",
]


class BorderSideWidth(
    BorderWidth,
):
    __metaclass__ = ABCMeta


class BorderTopWidth(
    BorderSideWidth,
):
    pass


class BorderRightWidth(
    BorderSideWidth,
):
    pass


class BorderBottomWidth(
    BorderSideWidth,
):
    pass


class BorderLeftWidth(
    BorderSideWidth,
):
    pass
