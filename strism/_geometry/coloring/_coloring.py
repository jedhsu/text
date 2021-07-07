"""

    *Coloring*

  An element's coloring.

"""

from dataclasses import dataclass

__all__ = [
    "Coloring",
]


@dataclass
class Coloring:
    foreground: ForegroundColor
    background: BackgroundColor
    image: Optional[BackgroundImage]
