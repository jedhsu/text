"""

    *Middle-West 4*   |⠗|

  The middle-west four gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ...west import WesternGi
from ..._number import FourGi
from .._gi import MiddleGi

__all__ = ["MiddleWest4"]


@dataclass
class MiddleWest4(
    Gi,
    MiddleGi,
    WesternGi,
    FourGi,
):
    symbol = "\u2817"
