"""

    *North-West 7*   ⠨

  The north-west seven gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import SevenGi
from .._gi import NorthernGi

__all__ = ["NorthWest7"]


@dataclass
class NorthWest7(
    Gi,
    StrismicGi,
    NorthernGi,
    WesternGi,
    SevenGi,
):
    symbol = "\u2828"
