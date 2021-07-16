"""

    *North-West 5*   ⠨

  The north-west five gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import FiveGi
from .._gi import NorthernGi

__all__ = ["NorthWest5"]


@dataclass
class NorthWest5(
    Gi,
    StrismicGi,
    NorthernGi,
    WesternGi,
    FiveGi,
):
    symbol = "\u2828"
