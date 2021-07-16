"""

    *North-East 5*   ⠨

  The north-east five gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import FiveGi
from .._gi import NorthernGi

__all__ = ["NorthEast5"]


@dataclass
class NorthEast5(
    Gi,
    StrismicGi,
    NorthernGi,
    EasternGi,
    FiveGi,
):
    symbol = "\u2828"
