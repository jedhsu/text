"""

    Face

  Face contains the stylistic graphical attributes of text.

"""

from dataclasses import dataclass

from .font import TextFont
from .coloring import TextColoring
from .lining import TextLining
from .boxing import TextBoxing

__all__ = [
    "TextFace",
]


@dataclass
class TextFace:
    font: TextFont
    coloring: TextColoring
    lining: TextLining
    boxing: TextBoxing
