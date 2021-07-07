"""

    *Font-Spacing*

  Describes the horizontal spacing of text.

"""

from enum import Enum

__all__ = ["FontSpacing"]


class Syntax:
    # css syntax
    syntax = "font-stretch"


class FontSpacing(
    Enum,
    Syntax,
):
    Normal = "normal"

    UltraCondensed = "ultra-condensed"
    ExtraCondensed = "extra-condensed"
    Condensed = "condensed"
    SemiCondensed = "semi-condensed"

    SemiExpanded = "semi-expanded"
    Expanded = "expanded"
    ExtraExpanded = "extra-expanded"
    UltraExpanded = "ultra-expanded"
