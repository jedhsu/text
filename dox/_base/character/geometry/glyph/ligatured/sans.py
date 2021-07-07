"""

    *Character Sans-Serif Glyph*

  A character glyph type with no ligatures.

"""

from abc import ABCMeta

from ._glyph import CharacterLigaturedGlyph

__all__ = ["CharacterSansSerifGlyph"]


class CharacterSansSerifGlyph(
    CharacterLigaturedGlyph,
):
    __metaclass__ = ABCMeta
