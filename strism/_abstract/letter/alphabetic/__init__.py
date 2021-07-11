"""

    *abs . lt . alph*

  Abstract alphabetic letter types.

"""

from ._alphabetic import Alphabetic

from ._letter import AbstractAlphabeticLetter
from .space import AbstractAlphabeticSpace

__all__ = [
    "Alphabetic",
    "AbstractAlphabeticLetter",
    "AbstractAlphabeticSpace",
]
