"""

    *abstract character*

"""

from ._character import AbstractCharacter
from .space import AbstractCharacterSpace

from .alphabetic import Alphabetic
from .alphabetic import AbstractAlphabeticCharacter
from .alphabetic import AbstractAlphabeticSpace

__all__ = [
    "AbstractCharacter",
    "AbstractCharacterSpace",
    "Alphabetic",
    "AbstractAlphabeticCharacter",
    "AbstractAlphabeticSpace",
]
