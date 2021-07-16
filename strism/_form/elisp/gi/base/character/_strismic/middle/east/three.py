"""

    *Middle-East 3*   |⠸|

  The middle-east three gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ...east import EasternGi
from ..._number import ThreeGi
from .._gi import MiddleGi

__all__ = ["MiddleEast3"]


@dataclass
class MiddleEast3(
    Gi,
    MiddleGi,
    EasternGi,
    ThreeGi,
):
    symbol = "\u2838"
