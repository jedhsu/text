"""

    Window Fringes

  The left and right window fringes.

"""

from dataclasses import dataclass

from ._fringe import WindowFringe

__all__ = [
    "WindowFringes",
]


@dataclass
class WindowFringes:
    left: WindowFringe
    right: WindowFringe
