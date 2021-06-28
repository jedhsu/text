"""

Text Align Last Line

Horizontal text alignment of the last line.

"""

__all__ = ["TextAlignLastLine"]

from enum import Enum


class TextAlignLastLineOption(
    Enum,
):
    Auto = "auto"

    Start = "start"
    End = "end"

    Left = "left"
    Center = "center"
    Right = "right"

    Justify = "justify"


class TextAlignLastLine(
    BlockElementOperator,
):

    pass
