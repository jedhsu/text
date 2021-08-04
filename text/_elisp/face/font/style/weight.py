"""

    Font Weight

  The density of a font.

"""

from enum import Enum

__all__ = [
    "FontWeight",
]


class FontWeight(
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
