"""

    *Upper-West Capital 4*   ⠨

  The upper-west capital four gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import FourGi
from ..._gi import UpperGi

__all__ = ["UpperWestCapital4"]


@dataclass
class UpperWestCapital4(
    Gi,
    StrismicGi,
    UpperGi,
    WesternGi,
    CapitalGi,
    FourGi,
):
    symbol = "\u2828"
