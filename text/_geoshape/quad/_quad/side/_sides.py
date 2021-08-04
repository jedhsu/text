"""

    *Quad Sides*

  The sides of a quad.

"""

from dataclasses import dataclass

from .top import QuadTopSide
from .right import QuadRightSide
from .bottom import QuadBottomSide
from .left import QuadLeftSide

__all__ = ["QuadSides"]


@dataclass
class QuadSides:
    top: QuadTopSide
    right: QuadRightSide
    bottom: QuadBottomSide
    left: QuadLeftSide
