"""

    *North-East Capital 6*   ⠨

  The north-east capital six gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import SixGi
from ..._gi import NorthernGi

__all__ = ["NorthEastCapital6"]


@dataclass
class NorthEastCapital6(
    Gi,
    StrismicGi,
    NorthernGi,
    EasternGi,
    CapitalGi,
    SixGi,
):
    symbol = "\u2828"
