"""

    *Quad Side Midpoints*

  The midpoints of the sides of a quad.

"""

from dataclasses import dataclass

from .top import QuadTopMidpoint
from .right import QuadRightMidpoint
from .bottom import QuadBottomMidpoint
from .left import QuadLeftMidpoint

__all__ = ["QuadSideMidpoints"]


@dataclass
class QuadSideMidpoints:
    top: QuadTopMidpoint
    right: QuadRightMidpoint
    bottom: QuadBottomMidpoint
    left: QuadLeftMidpoint
