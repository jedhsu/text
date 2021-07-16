"""

    *North-East Capital 1*   ⠨

  The north-east capital one gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import OneGi
from ..._gi import NorthernGi

__all__ = ["NorthEastCapital1"]


@dataclass
class NorthEastCapital1(
    Gi,
    StrismicGi,
    NorthernGi,
    EasternGi,
    CapitalGi,
    OneGi,
):
    symbol = "\u2828"
