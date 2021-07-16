"""

    *Middle-West 1*   ⠨

  The middle-west one gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ...west import WesternGi
from ..._number import OneGi
from .._gi import MiddleGi

__all__ = ["MiddleWest1"]


@dataclass
class MiddleWest1(
    Gi,
    MiddleGi,
    WesternGi,
    OneGi,
):
    symbol = "\u2828"
