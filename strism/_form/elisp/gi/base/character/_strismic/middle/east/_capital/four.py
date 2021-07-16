"""

    *Middle-East Capital 4*   ⠨

  The middle-east capital four gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import FourGi
from ..._gi import MiddleGi

__all__ = ["MiddleEastCapital4"]


@dataclass
class MiddleEastCapital4(
    Gi,
    StrismicGi,
    MiddleGi,
    EasternGi,
    CapitalGi,
    FourGi,
):
    symbol = "\u2828"
