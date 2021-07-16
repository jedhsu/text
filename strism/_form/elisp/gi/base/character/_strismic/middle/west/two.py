"""

    *MiddleWest2*   ⠨

  The middle-west two gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import TwoGi
from .._gi import MiddleGi

__all__ = ["MiddleWest2"]


@dataclass
class MiddleWest2(
    Gi,
    StrismicGi,
    MiddleGi,
    WesternGi,
    TwoGi,
):
    symbol = "\u2828"
