"""

    *Offset-Direction-Magnitude*

  Offset magnitude amounts

"""


from abc import ABCMeta

from ._magnitude import OffsetMagnitude

__all__ = [
    "OffsetDirectionMagnitude",
    "OffsetUpMagnitude",
    "OffsetRightMagnitude",
    "OffsetBottomMagnitude",
    "OffsetLeftMagnitude",
]


class OffsetDirectionMagnitude(
    OffsetMagnitude,
):
    __metaclass__ = ABCMeta


class OffsetUpMagnitude(
    OffsetDirectionMagnitude,
):
    pass


class OffsetRightMagnitude(
    OffsetDirectionMagnitude,
):
    pass


class OffsetDownMagnitude(
    OffsetDirectionMagnitude,
):
    pass


class OffsetLeftMagnitude(
    OffsetDirectionMagnitude,
):
    pass
