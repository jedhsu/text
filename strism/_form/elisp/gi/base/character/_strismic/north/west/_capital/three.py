"""

    *North-West Capital 3*   ⠨

  The north-west capital three gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import ThreeGi
from ..._gi import NorthernGi

__all__ = ["NorthWestCapital3"]


@dataclass
class NorthWestCapital3(
    Gi,
    StrismicGi,
    NorthernGi,
    WesternGi,
    CapitalGi,
    ThreeGi,
):
    symbol = "\u2828"
