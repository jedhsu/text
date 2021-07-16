"""

    *Upper-East Capital 5*   ⠨

  The upper-east capital five gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import FiveGi
from ..._gi import UpperGi

__all__ = ["UpperEastCapital5"]


@dataclass
class UpperEastCapital5(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    CapitalGi,
    FiveGi,
):
    symbol = "\u2828"
