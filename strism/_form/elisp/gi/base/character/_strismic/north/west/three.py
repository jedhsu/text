"""

    *NorthWest3*   ⠨

  The north-west three gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import ThreeGi
from .._gi import NorthernGi

__all__ = ["NorthWest3"]


@dataclass
class NorthWest3(
    Gi,
    StrismicGi,
    NorthernGi,
    WesternGi,
    ThreeGi,
):
    symbol = "\u2828"
