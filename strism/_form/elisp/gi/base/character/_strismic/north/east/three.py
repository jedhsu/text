"""

    *North-East 3*   ⠨

  The north-east three gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import ThreeGi
from .._gi import NorthernGi

__all__ = ["NorthEast3"]


@dataclass
class NorthEast3(
    Gi,
    StrismicGi,
    NorthernGi,
    EasternGi,
    ThreeGi,
):
    symbol = "\u2828"
