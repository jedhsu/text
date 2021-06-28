"""

HorizontalTextAlignment

Horizontal text alignment.

"""

__all__ = ["HorizontalTextAlignment"]

from dataclasses import dataclass
from enum import Enum


class HorizontalTextAlignment(
    Enum,
):
    Start = "start"
    End = "end"

    Left = "left"
    Right = "right"
    Center = "center"
    Justify = "justify"

    MatchParent = "match-parent"
    StartEnd = "start end"


@dataclass
class _Align_:
    combine_upright: type

    justify: type
    orientation: TextOrientation
    indent: Length
