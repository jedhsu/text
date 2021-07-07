"""

    *Block Spacing*

  Describes the spacing between lines (block elements).


"""

__all__ = ["BlockSpacing"]

from dataclasses import dataclass
from enum import Enum

syntax = "vertical-text-alignment"


class VerticalTextAlignmentOption(
    Enum,
):
    Baseline = "baseline"
    Subscript = "sub"
    Superscript = "super"

    Top = "top"
    Middle = "middle"
    Bottom = "bottom"

    TextTop = "text-top"
    TextBottom = "text-bottom"


# [TODO] finish


@dataclass
class VerticalTextAlignment(
    InlineElementOperator,
    TableCellOperator,
):
    def __init__(self):
        pass


@dataclass
class _Align_:
    combine_upright: type

    justify: type
    orientation: TextOrientation
    indent: Length
