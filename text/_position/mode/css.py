"""

    *Cascade: Position*

"""

from enum import Enum

from strism._form.cascade import CascadeProperty

__all__ = ["Position"]


class Position(
    Enum,
    CascadeProperty,
):
    Static = "static"
    Relative = "relative"
    Absolute = "absolute"
    Fixed = "fixed"
    Sticky = "sticky"
