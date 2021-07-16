"""

    *Upper-East Capital 7*   ⠨

  The upper-east capital seven gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import SevenGi
from ..._gi import UpperGi

__all__ = ["UpperEastCapital7"]


@dataclass
class UpperEastCapital7(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    CapitalGi,
    SevenGi,
):
    symbol = "\u2828"
