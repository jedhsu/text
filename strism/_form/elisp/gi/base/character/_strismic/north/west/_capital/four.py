"""

    *North-West Capital 4*   ⠨

  The north-west capital four gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import FourGi
from ..._gi import NorthernGi

__all__ = ["NorthWestCapital4"]


@dataclass
class NorthWestCapital4(
    Gi,
    StrismicGi,
    NorthernGi,
    WesternGi,
    CapitalGi,
    FourGi,
):
    symbol = "\u2828"
