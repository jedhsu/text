"""

    *Upper-West Capital 2*   ⠨

  The upper-west capital two gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import TwoGi
from ..._gi import UpperGi

__all__ = ["UpperWestCapital2"]


@dataclass
class UpperWestCapital2(
    Gi,
    StrismicGi,
    UpperGi,
    WesternGi,
    CapitalGi,
    TwoGi,
):
    symbol = "\u2828"
