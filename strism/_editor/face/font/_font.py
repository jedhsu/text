"""

    Text Font

  The font of text.

"""

from dataclasses import dataclass

from .family import FontFamily
from .shape import FontShape
from .style import FontStyle


@dataclass
class TextFont:
    family: FontFamily
    shape: FontShape
    style: FontStyle
