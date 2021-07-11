"""

    *Font Stroking*

  Partitions character glyph by "stroking".

  # [TODO] explain better

"""

from abc import ABCMeta

from .._font import FontStyle

__all__ = ["FontStroking"]


class FontStroking(
    FontStyle,
):
    __metaclass__ = ABCMeta
