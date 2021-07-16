"""

    *Upper-East Capital 1*   ⠨

  The upper-east capital one gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import OneGi
from ..._gi import UpperGi

__all__ = ["UpperEastCapital1"]


@dataclass
class UpperEastCapital1(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    CapitalGi,
    OneGi,
):
    symbol = "\u2828"
