"""

    *North-West 1*   ⠨

  The north-west one gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import OneGi
from .._gi import NorthernGi

__all__ = ["NorthWest1"]


@dataclass
class NorthWest1(
    Gi,
    StrismicGi,
    NorthernGi,
    WesternGi,
    OneGi,
):
    symbol = "\u2828"
