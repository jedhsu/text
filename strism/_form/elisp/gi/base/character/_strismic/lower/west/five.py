"""

    *Lower-West 5*   |⠷|

  The lower-west five gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import FiveGi
from .._gi import LowerGi

__all__ = ["LowerWest5"]


@dataclass
class LowerWest5(
    Gi,
    StrismicGi,
    LowerGi,
    WesternGi,
    FiveGi,
):
    symbol = "\u2837"
