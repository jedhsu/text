"""

    *Letter Ligatured-Glyph*

  Partitions character glyph by ligature type.

"""

from abc import ABCMeta

from .._glyph import LetterGlyph

__all__ = ["LetterLigaturedGlyph"]


class LetterLigaturedGlyph(
    LetterGlyph,
):
    __metaclass__ = ABCMeta
