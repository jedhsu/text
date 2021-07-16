"""

    *North-West 6*   ⠨

  The north-west six gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import SixGi
from .._gi import NorthernGi

__all__ = ["NorthWest6"]


@dataclass
class NorthWest6(
    Gi,
    StrismicGi,
    NorthernGi,
    WesternGi,
    SixGi,
):
    symbol = "\u2828"
