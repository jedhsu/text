"""

    *North-West Capital 7*   ⠨

  The north-west capital seven gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import SevenGi
from ..._gi import NorthernGi

__all__ = ["NorthWestCapital7"]


@dataclass
class NorthWestCapital7(
    Gi,
    StrismicGi,
    NorthernGi,
    WesternGi,
    CapitalGi,
    SevenGi,
):
    symbol = "\u2828"
