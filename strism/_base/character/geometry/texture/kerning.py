"""

    *Font-Kerning*

  A type of font texture describing ligature connections.

"""

from enum import Enum

from ._texture import FontLigatureTexture

__all__ = ["FontKerning"]


class FontKerning(
    FontLigatureTexture,
    Enum,
):
    Auto = "Auto"
    Normal = "Normal"
    None_ = "None"
