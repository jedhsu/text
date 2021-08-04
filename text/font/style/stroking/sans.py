"""

    *Sans-Serif Stroking*

  A font with no "extension strokes".

"""

from abc import ABCMeta

from ._font import FontStroking

__all__ = ["SansSerifStroking"]


class SansSerifStroking(
    FontStroking,
):
    __metaclass__ = ABCMeta
