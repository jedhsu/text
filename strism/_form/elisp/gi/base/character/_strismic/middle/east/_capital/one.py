"""

    *Middle-East Capital 1*   ⠨

  The middle-east capital one gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import OneGi
from ..._gi import MiddleGi

__all__ = ["MiddleEastCapital1"]


@dataclass
class MiddleEastCapital1(
    Gi,
    StrismicGi,
    MiddleGi,
    EasternGi,
    CapitalGi,
    OneGi,
):
    symbol = "\u2828"
