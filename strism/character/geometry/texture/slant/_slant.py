"""

    *Character Slant*

  Describes the diagonal slant of character glyphs.

"""

__all__ = ["FontSlant"]


class Syntax:
    Css = "font-style"
    Elisp = "font-slant"


class FontSlant(
    Syntax,
):
    Normal = "Normal"
    Italic = "Italic"
    Oblique = "Oblique"

    Inherit = "Inherit"

    ReverseItalic = "reverse-italic"
    ReverseOblique = "reverse-oblique"
