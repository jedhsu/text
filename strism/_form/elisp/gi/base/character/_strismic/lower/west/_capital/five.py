"""

    *Lower-West Capital 5*   ⠨

  The lower-west capital five gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import FiveGi
from ..._gi import LowerGi

__all__ = ["LowerWestCapital5"]


@dataclass
class LowerWestCapital5(
    Gi,
    StrismicGi,
    LowerGi,
    WesternGi,
    CapitalGi,
    FiveGi,
):
    symbol = "\u2828"
