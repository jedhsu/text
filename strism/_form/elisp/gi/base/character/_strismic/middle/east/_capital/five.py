"""

    *Middle-East Capital 5*   ⠨

  The middle-east capital five gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import FiveGi
from ..._gi import MiddleGi

__all__ = ["MiddleEastCapital5"]


@dataclass
class MiddleEastCapital5(
    Gi,
    StrismicGi,
    MiddleGi,
    EasternGi,
    CapitalGi,
    FiveGi,
):
    symbol = "\u2828"
