"""

    *Lower-West Capital 4*   ⠨

  The lower-west capital four gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import FourGi
from ..._gi import LowerGi

__all__ = ["LowerWestCapital4"]


@dataclass
class LowerWestCapital4(
    Gi,
    StrismicGi,
    LowerGi,
    WesternGi,
    CapitalGi,
    FourGi,
):
    symbol = "\u2828"
