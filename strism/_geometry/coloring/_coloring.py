"""

    *Coloring*

  An element's coloring.

"""

from dataclasses import dataclass

from typing import Optional

from .background import BackgroundColor
from .foreground import ForegroundColor

__all__ = ["Coloring"]


@dataclass
class Coloring:
    foreground: ForegroundColor
    background: BackgroundColor
    image: Optional[BackgroundImage]
