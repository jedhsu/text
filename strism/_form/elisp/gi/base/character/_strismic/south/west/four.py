"""

    *SouthWest4*   ⠨

  The south-west four gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import FourGi
from .._gi import SouthernGi

__all__ = ["SouthWest4"]


@dataclass
class SouthWest4(
    Gi,
    StrismicGi,
    SouthernGi,
    WesternGi,
    FourGi,
):
    symbol = "\u2828"
