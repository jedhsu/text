"""

    *Upper-East Capital 3*   ⠨

  The upper-east capital three gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import ThreeGi
from ..._gi import UpperGi

__all__ = ["UpperEastCapital3"]


@dataclass
class UpperEastCapital3(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    CapitalGi,
    ThreeGi,
):
    symbol = "\u2828"
