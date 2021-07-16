"""

    *Middle-East 6*

  The middle-east six gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ...east import EasternGi
from ..._number import SixGi
from .._gi import MiddleGi

__all__ = ["MiddleEast6"]


@dataclass
class MiddleEast6(
    Gi,
    MiddleGi,
    EasternGi,
    SixGi,
):
    symbol = "\u2828"
