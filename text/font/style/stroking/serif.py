"""

    *Serif Stroking*

  A font with "extension strokes".

"""

from abc import ABCMeta

from ._font import FontStroking

__all__ = ["SerifStroking"]


class SerifStroking(
    FontStroking,
):
    __metaclass__ = ABCMeta
