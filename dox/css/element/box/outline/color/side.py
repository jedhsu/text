"""

    *Outline-Side-Color*

  Outline side color.

"""


from abc import ABCMeta

from ._color import OutlineColor

__all__ = [
    "OutlineSideColor",
    "OutlineTopColor",
    "OutlineRightColor",
    "OutlineBottomColor",
    "OutlineLeftColor",
]


class OutlineSideColor(
    OutlineColor,
):
    __metaclass__ = ABCMeta


class OutlineTopColor(
    OutlineSideColor,
):
    pass


class OutlineRightColor(
    OutlineSideColor,
):
    pass


class OutlineBottomColor(
    OutlineSideColor,
):
    pass


class OutlineLeftColor(
    OutlineSideColor,
):
    pass
