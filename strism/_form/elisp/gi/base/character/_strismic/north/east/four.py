"""

    *North-East 4*   ⠨

  The north-east four gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import FourGi
from .._gi import NorthernGi

__all__ = ["NorthEast4"]


@dataclass
class NorthEast4(
    Gi,
    StrismicGi,
    NorthernGi,
    EasternGi,
    FourGi,
):
    symbol = "\u2828"
