"""

    *Upper-West Capital 5*   ⠨

  The upper-west capital five gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import FiveGi
from ..._gi import UpperGi

__all__ = ["UpperWestCapital5"]


@dataclass
class UpperWestCapital5(
    Gi,
    StrismicGi,
    UpperGi,
    WesternGi,
    CapitalGi,
    FiveGi,
):
    symbol = "\u2828"
