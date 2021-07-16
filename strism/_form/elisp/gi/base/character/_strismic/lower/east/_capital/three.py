"""

    *Lower-East Capital 3*   ⠨

  The lower-east capital three gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import ThreeGi
from ..._gi import LowerGi

__all__ = ["LowerEastCapital3"]


@dataclass
class LowerEastCapital3(
    Gi,
    StrismicGi,
    LowerGi,
    EasternGi,
    CapitalGi,
    ThreeGi,
):
    symbol = "\u2828"
