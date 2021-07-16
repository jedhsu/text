"""

    *North-East Capital 4*   ⠨

  The north-east capital four gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import FourGi
from ..._gi import NorthernGi

__all__ = ["NorthEastCapital4"]


@dataclass
class NorthEastCapital4(
    Gi,
    StrismicGi,
    NorthernGi,
    EasternGi,
    CapitalGi,
    FourGi,
):
    symbol = "\u2828"
