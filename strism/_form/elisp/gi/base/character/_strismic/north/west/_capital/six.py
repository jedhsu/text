"""

    *North-West Capital 6*   ⠨

  The north-west capital six gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import SixGi
from ..._gi import NorthernGi

__all__ = ["NorthWestCapital6"]


@dataclass
class NorthWestCapital6(
    Gi,
    StrismicGi,
    NorthernGi,
    WesternGi,
    CapitalGi,
    SixGi,
):
    symbol = "\u2828"
