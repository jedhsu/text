"""

    *Middle-East Capital 2*   ⠨

  The middle-east capital two gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import TwoGi
from ..._gi import MiddleGi

__all__ = ["MiddleEastCapital2"]


@dataclass
class MiddleEastCapital2(
    Gi,
    StrismicGi,
    MiddleGi,
    EasternGi,
    CapitalGi,
    TwoGi,
):
    symbol = "\u2828"
