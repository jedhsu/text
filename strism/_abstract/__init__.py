"""

    *abst*

  Abstract objects.

"""

from ._element import AbstractElement

from .character import AbstractCharacter
from .string import AbstractString
from .word import AbstractWord
from .chunk import AbstractChunk
from .line import AbstractLine
from .shape import AbstractShape
from .block import AbstractBlock
from .page import AbstractPage

__all__ = [
    "AbstractElement",
    "AbstractCharacter",
    "AbstractString",
    "AbstractWord",
    "AbstractChunk",
    "AbstractLine",
    "AbstractShape",
    "AbstractBlock",
    "AbstractPage",
]
