"""

    Font Shape

  The shape of the font.

"""


from dataclasses import dataclass

from .height import FontHeight
from .width import FontWidth

__all__ = [
    "FontShape",
]


@dataclass
class FontShape:
    height: FontHeight
    width: FontWidth
