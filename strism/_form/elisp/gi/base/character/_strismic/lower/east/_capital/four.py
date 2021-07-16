"""

    *Lower-East Capital 4*   ⠨

  The lower-east capital four gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import FourGi
from ..._gi import LowerGi

__all__ = ["LowerEastCapital4"]


@dataclass
class LowerEastCapital4(
    Gi,
    StrismicGi,
    LowerGi,
    EasternGi,
    CapitalGi,
    FourGi,
):
    symbol = "\u2828"
