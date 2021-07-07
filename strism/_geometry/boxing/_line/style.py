"""

    *Line-Style*

  Style for a generic line.

"""

from abc import ABCMeta

from enum import Enum

__all__ = ["LineStyle"]


class LineStyle(
    Enum,
):
    __metaclass__ = ABCMeta

    Nothing = "Nothing"
    Hidden = "Hidden"
    Solid = "Solid"
    Dotted = "Dotted"
    Dashed = "Dashed"
    Double = "Double"
    Groove = "Groove"
    Ridge = "Ridge"
    Inset = "Inset"
    Outset = "Outset"
