"""

    *geo . box . bord . clr . side*

  Border-side color types.

"""

from ._side import BorderSideColor

from .top import BorderTopColor
from .right import BorderRightColor
from .bottom import BorderBottomColor
from .left import BorderLeftColor

__all__ = [
    "BorderSideColor",
    "BorderTopColor",
    "BorderRightColor",
    "BorderBottomColor",
    "BorderLeftColor",
]
