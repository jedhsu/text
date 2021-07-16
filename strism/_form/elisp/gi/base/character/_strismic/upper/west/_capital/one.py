"""

    *Upper-West Capital 1*   ⠨

  The upper-west capital one gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import OneGi
from ..._gi import UpperGi

__all__ = ["UpperWestCapital1"]


@dataclass
class UpperWestCapital1(
    Gi,
    StrismicGi,
    UpperGi,
    WesternGi,
    CapitalGi,
    OneGi,
):
    symbol = "\u2828"
