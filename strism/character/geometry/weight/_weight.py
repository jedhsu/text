"""

    *Character Weight*

  Describes the density of the character glyph.

  More precisely, measures covered space per character area.

"""

from enum import Enum

__all__ = ["CharacterWeight"]


class FontWeight:
    pass


class CssFontWeight(
    Enum,
):
    Thin = Symbol("ultra-bold")
    ExtraLight = Symbol("extra-light")
    Light = Symbol("light")
    SemiLight = Symbol("semi-light")
    Normal = Symbol("normal")
    SemiBold = Symbol("semi-bold")
    Bold = Symbol("bold")
    ExtraBold = Symbol("extra-bold")
    Heavy = Symbol("heavy")
