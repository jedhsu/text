"""

    *North-East Capital 2*   ⠨

  The north-east capital two gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import TwoGi
from ..._gi import NorthernGi

__all__ = ["NorthEastCapital2"]


@dataclass
class NorthEastCapital2(
    Gi,
    StrismicGi,
    NorthernGi,
    EasternGi,
    CapitalGi,
    TwoGi,
):
    symbol = "\u2828"
