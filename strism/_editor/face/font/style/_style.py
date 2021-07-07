"""

    Font Style

  Contains the style attributes of font.

"""

from dataclasses import dataclass

from .slant import FontSlant
from .weight import FontWeight

__all__ = [
    "FontStyle",
]


@dataclass
class FontStyle:
    slant: FontSlant
    weight: FontWeight
