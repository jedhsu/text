"""

    *Lower-East Capital 2*   ⠨

  The lower-east capital two gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import TwoGi
from ..._gi import LowerGi

__all__ = ["LowerEastCapital2"]


@dataclass
class LowerEastCapital2(
    Gi,
    StrismicGi,
    LowerGi,
    EasternGi,
    CapitalGi,
    TwoGi,
):
    symbol = "\u2828"
