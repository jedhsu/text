"""

    *Middle-West Capital 2*   ⠨

  The middle-west capital two gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import TwoGi
from ..._gi import MiddleGi

__all__ = ["MiddleWestCapital2"]


@dataclass
class MiddleWestCapital2(
    Gi,
    StrismicGi,
    MiddleGi,
    WesternGi,
    CapitalGi,
    TwoGi,
):
    symbol = "\u2828"
