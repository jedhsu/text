"""

    *Letter Fantasy Glyph*

  A fantasy character glyph type.

"""

from abc import ABCMeta

from ._glyph import LetterGlyph


class LetterFantasyGlyph(
    LetterGlyph,
):
    __metaclass__ = ABCMeta
