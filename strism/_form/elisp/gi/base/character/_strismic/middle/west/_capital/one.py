"""

    *Middle-West Capital 1*   ⠨

  The middle-west capital one gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import OneGi
from ..._gi import MiddleGi

__all__ = ["MiddleWestCapital1"]


@dataclass
class MiddleWestCapital1(
    Gi,
    StrismicGi,
    MiddleGi,
    WesternGi,
    CapitalGi,
    OneGi,
):
    symbol = "\u2828"
