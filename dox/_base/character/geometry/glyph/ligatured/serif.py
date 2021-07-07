"""

    *Character Serif Glyph*

  A character glyph type with ligatures.

"""

from abc import ABCMeta

from ._glyph import CharacterLigaturedGlyph

__all__ = ["CharacterSerifGlyph"]


class CharacterSerifGlyph(
    CharacterLigaturedGlyph,
):
    __metaclass__ = ABCMeta
