"""

    *Lower-West Capital 1*   ⠨

  The lower-west capital one gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import OneGi
from ..._gi import LowerGi

__all__ = ["LowerWestCapital1"]


@dataclass
class LowerWestCapital1(
    Gi,
    StrismicGi,
    LowerGi,
    WesternGi,
    CapitalGi,
    OneGi,
):
    symbol = "\u2828"
