"""

    *Letter Glyph*

  Maps each letter to a spatial glyph.

  This is traditionally font.

"""

from abc import ABCMeta

from .._geometra import LetterGeometra

__all__ = ["LetterGlyph"]


class LetterGlyph(
    LetterGeometra,
):
    __metaclass__ = ABCMeta
