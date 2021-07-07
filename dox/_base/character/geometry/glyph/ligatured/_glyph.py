"""

    *Character Ligatured-Glyph*

  Partitions character glyph by ligature type.

"""

from abc import ABCMeta

from .._glyph import CharacterGlyph

__all__ = ["CharacterLigaturedGlyph"]


class CharacterLigaturedGlyph(
    CharacterGlyph,
):
    __metaclass__ = ABCMeta
