"""

    *Upper-East Capital 6*   ⠨

  The upper-east capital six gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import SixGi
from ..._gi import UpperGi

__all__ = ["UpperEastCapital6"]


@dataclass
class UpperEastCapital6(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    CapitalGi,
    SixGi,
):
    symbol = "\u2828"
