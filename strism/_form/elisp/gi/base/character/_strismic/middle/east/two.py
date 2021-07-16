"""

    *Middle-East 2*   |⠨|

  The middle-east two gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import TwoGi
from .._gi import MiddleGi

__all__ = ["MiddleEast2"]


@dataclass
class MiddleEast2(
    Gi,
    StrismicGi,
    MiddleGi,
    EasternGi,
    TwoGi,
):
    symbol = "\u2828"
