"""

    *graphical color*

  Spectral color measures.

"""

from ._color import Color

from .rgba import Rgba
from .hsva import Hsba

__all__ = [
    "Color",
    "Rgba",
    "Hsba",
]
