"""

    *SouthWest2*   ⠨

  The south-west two gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import TwoGi
from .._gi import SouthernGi

__all__ = ["SouthWest2"]


@dataclass
class SouthWest2(
    Gi,
    StrismicGi,
    SouthernGi,
    WesternGi,
    TwoGi,
):
    symbol = "\u2828"
