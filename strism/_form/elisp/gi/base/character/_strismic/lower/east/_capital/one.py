"""

    *Lower-East Capital 1*   ⠨

  The lower-east capital one gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....east import EasternGi
from ...._number import OneGi
from ..._gi import LowerGi

__all__ = ["LowerEastCapital1"]


@dataclass
class LowerEastCapital1(
    Gi,
    StrismicGi,
    LowerGi,
    EasternGi,
    CapitalGi,
    OneGi,
):
    symbol = "\u2828"
