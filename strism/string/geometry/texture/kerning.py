"""

    *String Kerning*

  A string texture describing how a subset of characters visually connect.

"""

from enum import Enum

from ._texture import StringTexture

__all__ = ["StringKerning"]


class StringKerning(
    StringTexture,
    CssProperty,
    Enum,
):
    Auto = "Auto"
    Normal = "Normal"
    None_ = "None"
