"""

    *North-East Capital 5*   ⠨

  The north-east capital five gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import FiveGi
from ..._gi import NorthernGi

__all__ = ["NorthEastCapital5"]


@dataclass
class NorthEastCapital5(
    Gi,
    StrismicGi,
    NorthernGi,
    EasternGi,
    CapitalGi,
    FiveGi,
):
    symbol = "\u2828"
