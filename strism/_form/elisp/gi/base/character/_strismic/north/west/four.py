"""

    *North-West 4*   ⠨

  The north-west four gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import FourGi
from .._gi import NorthernGi

__all__ = ["NorthWest4"]


@dataclass
class NorthWest4(
    Gi,
    StrismicGi,
    NorthernGi,
    WesternGi,
    FourGi,
):
    symbol = "\u2828"
