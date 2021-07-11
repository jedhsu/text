"""

    *abst*

  Abstract objects.

"""

from ._element import AbstractElement

from .letter import AbstractLetter
from .string import AbstractString
from .word import AbstractWord
from .chunk import AbstractChunk
from .line import AbstractLine
from .shape import AbstractShape
from .block import AbstractBlock
from .page import AbstractPage

__all__ = [
    "AbstractElement",
    "AbstractLetter",
    "AbstractString",
    "AbstractWord",
    "AbstractChunk",
    "AbstractLine",
    "AbstractShape",
    "AbstractBlock",
    "AbstractPage",
]
