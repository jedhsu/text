"""

    *Middle-East 5*   ⠨

  The middle-east five gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ...east import EasternGi
from ..._number import FiveGi
from .._gi import MiddleGi

__all__ = ["MiddleEast5"]


@dataclass
class MiddleEast5(
    Gi,
    MiddleGi,
    EasternGi,
    FiveGi,
):
    symbol = "\u2828"
