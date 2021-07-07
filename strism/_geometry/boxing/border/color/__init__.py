"""

    *geo . box . bord . clr*

  Border box color types.

"""

from ._color import BorderColor

from .side import BorderSideColor
from .side import BorderTopColor
from .side import BorderRightColor
from .side import BorderBottomColor
from .side import BorderLeftColor


__all__ = [
    "BorderSideColor",
    "BorderTopColor",
    "BorderRightColor",
    "BorderBottomColor",
    "BorderLeftColor",
]
