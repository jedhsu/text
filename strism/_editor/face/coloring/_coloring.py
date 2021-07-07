"""

    Text Coloring

  The coloring of text.

"""

from typing import Optional
from dataclasses import dataclass

from .foreground import ForegroundColor
from .background import BackgroundColor
from .altforeground import AltForegroundColor

__all__ = [
    "TextColoring",
]


@dataclass
class TextColoring:
    foreground: ForegroundColor
    background: BackgroundColor
    altforeground: Optional[AltForegroundColor]

    @classmethod
    def create(
        cls,
        foreground: ForegroundColor,
        background: BackgroundColor,
        altforeground: Optional[AltForegroundColor] = None,
    ):
        return cls(
            foreground,
            background,
            altforeground,
        )
