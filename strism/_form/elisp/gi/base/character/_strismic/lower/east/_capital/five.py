"""

    *Lower-East Capital 5*   ⠨

  The lower-east capital five gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import FiveGi
from ..._gi import LowerGi

__all__ = ["LowerEastCapital5"]


@dataclass
class LowerEastCapital5(
    Gi,
    StrismicGi,
    LowerGi,
    EasternGi,
    CapitalGi,
    FiveGi,
):
    symbol = "\u2828"
