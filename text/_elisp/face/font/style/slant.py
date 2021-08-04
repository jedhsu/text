"""

    Font Slant

  The slant of a font.

"""

from enum import Enum

__all__ = [
    "FontSlant",
]


class FontSlant(
    Enum,
):
    Italic = Symbol("italic")
    Oblique = Symbol("oblique")
    Normal = Symbol("normal")
    ReverseItalic = Symbol("reverse-italic")
    ReverseOblique = Symbol("reverse-oblique")
