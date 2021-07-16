"""

    *South-East 3*   ⠨

  The south-east three gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import ThreeGi
from .._gi import SouthernGi

__all__ = ["SouthEast3"]


@dataclass
class SouthEast3(
    Gi,
    StrismicGi,
    SouthernGi,
    EasternGi,
    ThreeGi,
):
    symbol = "\u2828"
