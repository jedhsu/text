"""

    *Character Fantasy Glyph*

  A fantasy character glyph type.

"""

from abc import ABCMeta

from ._glyph import CharacterGlyph


class CharacterFantasyGlyph(
    CharacterGlyph,
):
    __metaclass__ = ABCMeta
