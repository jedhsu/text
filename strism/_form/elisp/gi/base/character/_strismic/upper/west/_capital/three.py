"""

    *Upper-West Capital 3*   ⠨

  The upper-west capital three gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import ThreeGi
from ..._gi import UpperGi

__all__ = ["UpperWestCapital3"]


@dataclass
class UpperWestCapital3(
    Gi,
    StrismicGi,
    UpperGi,
    WesternGi,
    CapitalGi,
    ThreeGi,
):
    symbol = "\u2828"
