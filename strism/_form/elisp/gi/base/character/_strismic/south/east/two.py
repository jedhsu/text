"""

    *South-East 2*   ⠨

  The south-east two gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import TwoGi
from .._gi import SouthernGi

__all__ = ["SouthEast2"]


@dataclass
class SouthEast2(
    Gi,
    StrismicGi,
    SouthernGi,
    EasternGi,
    TwoGi,
):
    symbol = "\u2828"
