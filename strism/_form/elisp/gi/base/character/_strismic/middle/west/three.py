"""

    *Middle-West 3*   |⠇|

  The middle-west three gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ...west import WesternGi
from ..._number import ThreeGi
from .._gi import MiddleGi

__all__ = ["MiddleWest3"]


@dataclass
class MiddleWest3(
    Gi,
    MiddleGi,
    WesternGi,
    ThreeGi,
):
    symbol = "\u2807"
