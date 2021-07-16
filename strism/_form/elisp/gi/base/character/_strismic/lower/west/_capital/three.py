"""

    *Lower-West Capital 3*   ⠨

  The lower-west capital three gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import ThreeGi
from ..._gi import LowerGi

__all__ = ["LowerWestCapital3"]


@dataclass
class LowerWestCapital3(
    Gi,
    StrismicGi,
    LowerGi,
    WesternGi,
    CapitalGi,
    ThreeGi,
):
    symbol = "\u2828"
