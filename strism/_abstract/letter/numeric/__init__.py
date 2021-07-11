"""

    *abs . lt . num*

  Abstract numeric letter types.

"""

from ._numeric import Numeric

from ._letter import AbstractNumericLetter
from .space import AbstractNumericSpace

__all__ = [
    "Numeric",
    "AbstractNumericLetter",
    "AbstractNumericSpace",
]
