"""

    *Middle-West Capital 5*   ⠨

  The middle-west capital five gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import FiveGi
from ..._gi import MiddleGi

__all__ = ["MiddleWestCapital5"]


@dataclass
class MiddleWestCapital5(
    Gi,
    StrismicGi,
    MiddleGi,
    WesternGi,
    CapitalGi,
    FiveGi,
):
    symbol = "\u2828"
