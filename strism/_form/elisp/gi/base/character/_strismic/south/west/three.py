"""

    *SouthWest3*   ⠨

  The south-west three gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import ThreeGi
from .._gi import SouthernGi

__all__ = ["SouthWest3"]


@dataclass
class SouthWest3(
    Gi,
    StrismicGi,
    SouthernGi,
    WesternGi,
    ThreeGi,
):
    symbol = "\u2828"
