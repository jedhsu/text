"""

    *Position*

"""

from enum import Enum

__all__ = ["Position"]


class Position(
    Enum,
    Property,
):
    Static = "static"
    Relative = "relative"
    Absolute = "absolute"
    Fixed = "fixed"
    Sticky = "sticky"
