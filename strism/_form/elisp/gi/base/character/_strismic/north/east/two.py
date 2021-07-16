"""

    *North-East 2*   ⠨

  The north-east two gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import TwoGi
from .._gi import NorthernGi

__all__ = ["NorthEast2"]


@dataclass
class NorthEast2(
    Gi,
    StrismicGi,
    NorthernGi,
    EasternGi,
    TwoGi,
):
    symbol = "\u2828"
