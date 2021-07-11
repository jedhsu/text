"""

    *Quad Corners*

  The sides of a quad.

"""

from dataclasses import dataclass

from .topright import QuadTopRightCorner
from .bottomright import QuadBottomRightCorner
from .bottomleft import QuadBottomLeftCorner
from .topleft import QuadTopLeftCorner

__all__ = ["QuadCorners"]


@dataclass
class QuadCorners:
    topright: QuadTopRightCorner
    bottomright: QuadBottomRightCorner
    bottomleft: QuadBottomLeftCorner
    topleft: QuadTopLeftCorner
