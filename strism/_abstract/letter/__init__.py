"""

    *abs . lt*

  Abstract letter types.

"""

from ._letter import AbstractLetter
from .space import AbstractLetterSpace

from .alphabetic import Alphabetic
from .alphabetic import AbstractAlphabeticLetter
from .alphabetic import AbstractAlphabeticSpace

__all__ = [
    "AbstractLetter",
    "AbstractLetterSpace",
    "Alphabetic",
    "AbstractAlphabeticLetter",
    "AbstractAlphabeticSpace",
]
