"""

    *LowerWest4*   ⠨

  The lower-west four gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import FourGi
from .._gi import LowerGi

__all__ = ["LowerWest4"]


@dataclass
class LowerWest4(
    Gi,
    StrismicGi,
    LowerGi,
    WesternGi,
    FourGi,
):
    symbol = "\u2828"
