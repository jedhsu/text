"""

    *Middle-East Capital 6*   ⠨

  The middle-east capital six gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import SixGi
from ..._gi import MiddleGi

__all__ = ["MiddleEastCapital6"]


@dataclass
class MiddleEastCapital6(
    Gi,
    StrismicGi,
    MiddleGi,
    EasternGi,
    CapitalGi,
    SixGi,
):
    symbol = "\u2828"
