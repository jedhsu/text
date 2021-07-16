"""

    *North-East Capital 3*   ⠨

  The north-east capital three gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import ThreeGi
from ..._gi import NorthernGi

__all__ = ["NorthEastCapital3"]


@dataclass
class NorthEastCapital3(
    Gi,
    StrismicGi,
    NorthernGi,
    EasternGi,
    CapitalGi,
    ThreeGi,
):
    symbol = "\u2828"
