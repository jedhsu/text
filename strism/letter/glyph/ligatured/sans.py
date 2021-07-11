"""

    *Letter Sans-Serif Glyph*

  A character glyph type with no ligatures.

"""

from abc import ABCMeta

from ._glyph import LetterLigaturedGlyph

__all__ = ["LetterSansSerifGlyph"]


class LetterSansSerifGlyph(
    LetterLigaturedGlyph,
):
    __metaclass__ = ABCMeta
