"""

    *Lower-West Capital 2*   ⠨

  The lower-west capital two gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import TwoGi
from ..._gi import LowerGi

__all__ = ["LowerWestCapital2"]


@dataclass
class LowerWestCapital2(
    Gi,
    StrismicGi,
    LowerGi,
    WesternGi,
    CapitalGi,
    TwoGi,
):
    symbol = "\u2828"
