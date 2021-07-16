"""

    *Middle-East Capital 3*   ⠨

  The middle-east capital three gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import ThreeGi
from ..._gi import MiddleGi

__all__ = ["MiddleEastCapital3"]


@dataclass
class MiddleEastCapital3(
    Gi,
    StrismicGi,
    MiddleGi,
    EasternGi,
    CapitalGi,
    ThreeGi,
):
    symbol = "\u2828"
