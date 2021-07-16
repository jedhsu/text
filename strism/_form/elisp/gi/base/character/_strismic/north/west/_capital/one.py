"""

    *North-West Capital 1*   ⠨

  The north-west capital one gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import OneGi
from ..._gi import NorthernGi

__all__ = ["NorthWestCapital1"]


@dataclass
class NorthWestCapital1(
    Gi,
    StrismicGi,
    NorthernGi,
    WesternGi,
    CapitalGi,
    OneGi,
):
    symbol = "\u2828"
