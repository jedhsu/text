"""

    *NorthWest2*   ⠨

  The north-west two gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import TwoGi
from .._gi import NorthernGi

__all__ = ["NorthWest2"]


@dataclass
class NorthWest2(
    Gi,
    StrismicGi,
    NorthernGi,
    WesternGi,
    TwoGi,
):
    symbol = "\u2828"
