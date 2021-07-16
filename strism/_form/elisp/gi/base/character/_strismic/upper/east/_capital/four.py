"""

    *Upper-East Capital 4*   ⠨

  The upper-east capital four gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import FourGi
from ..._gi import UpperGi

__all__ = ["UpperEastCapital4"]


@dataclass
class UpperEastCapital4(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    CapitalGi,
    FourGi,
):
    symbol = "\u2828"
