"""

    *North-West Capital 2*   ⠨

  The north-west capital two gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import TwoGi
from ..._gi import NorthernGi

__all__ = ["NorthWestCapital2"]


@dataclass
class NorthWestCapital2(
    Gi,
    StrismicGi,
    NorthernGi,
    WesternGi,
    CapitalGi,
    TwoGi,
):
    symbol = "\u2828"
