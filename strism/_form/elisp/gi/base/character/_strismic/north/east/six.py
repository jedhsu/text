"""

    *North-East 6*   ⠨

  The north-east six gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import SixGi
from .._gi import NorthernGi

__all__ = ["NorthEast6"]


@dataclass
class NorthEast6(
    Gi,
    StrismicGi,
    NorthernGi,
    EasternGi,
    SixGi,
):
    symbol = "\u2828"
