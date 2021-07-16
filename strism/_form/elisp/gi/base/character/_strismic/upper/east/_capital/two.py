"""

    *Upper-East Capital 2*   ⠨

  The upper-east capital two gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import TwoGi
from ..._gi import UpperGi

__all__ = ["UpperEastCapital2"]


@dataclass
class UpperEastCapital2(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    CapitalGi,
    TwoGi,
):
    symbol = "\u2828"
