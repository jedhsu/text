"""

    *Upper-East Capital 8*   ⠨

  The upper-east capital eighteight

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import EightGi
from ..._gi import UpperGi

__all__ = ["UpperEastCapital8"]


@dataclass
class UpperEastCapital8(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    CapitalGi,
    EightGi,
):
    symbol = "\u2828"
