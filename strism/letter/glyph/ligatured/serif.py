"""

    *Letter Serif Glyph*

  A character glyph type with ligatures.

"""

from abc import ABCMeta

from ._glyph import LetterLigaturedGlyph

__all__ = ["LetterSerifGlyph"]


class LetterSerifGlyph(
    LetterLigaturedGlyph,
):
    __metaclass__ = ABCMeta
