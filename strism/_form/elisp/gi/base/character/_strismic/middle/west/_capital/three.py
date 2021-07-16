"""

    *Middle-West Capital 3*   ⠨

  The middle-west capital three gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import ThreeGi
from ..._gi import MiddleGi

__all__ = ["MiddleWestCapital3"]


@dataclass
class MiddleWestCapital3(
    Gi,
    StrismicGi,
    MiddleGi,
    WesternGi,
    CapitalGi,
    ThreeGi,
):
    symbol = "\u2828"
