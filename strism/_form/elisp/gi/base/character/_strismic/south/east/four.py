"""

    *South-East 4*   ⠨

  The south-east four gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import FourGi
from .._gi import SouthernGi

__all__ = ["SouthEast4"]


@dataclass
class SouthEast4(
    Gi,
    StrismicGi,
    SouthernGi,
    EasternGi,
    FourGi,
):
    symbol = "\u2828"
