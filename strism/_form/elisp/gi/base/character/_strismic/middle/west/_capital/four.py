"""

    *Middle-West Capital 4*   ⠨

  The middle-west capital four gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import FourGi
from ..._gi import MiddleGi

__all__ = ["MiddleWestCapital4"]


@dataclass
class MiddleWestCapital4(
    Gi,
    StrismicGi,
    MiddleGi,
    WesternGi,
    CapitalGi,
    FourGi,
):
    symbol = "\u2828"
