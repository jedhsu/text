"""

    *Middle-West 5*   |⠯|

  The middle-west five gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ...west import WesternGi
from ..._number import FiveGi
from .._gi import MiddleGi

__all__ = ["MiddleWest5"]


@dataclass
class MiddleWest5(
    Gi,
    MiddleGi,
    WesternGi,
    FiveGi,
):
    symbol = "\u282f"
