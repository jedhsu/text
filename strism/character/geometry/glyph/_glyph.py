"""

    *Character Glyph*

  Maps each abstract character to a visual glyph.

  This is traditionally font.

"""

from abc import ABCMeta

from .._geometric import CharacterGeometric

__all__ = ["CharacterGlyph"]


class CharacterGlyph(
    CharacterGeometric,
):
    __metaclass__ = ABCMeta
