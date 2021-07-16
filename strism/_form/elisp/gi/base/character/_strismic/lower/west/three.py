"""

    *Lower-West 3*   |⠦|

  The lower-west three gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import ThreeGi
from .._gi import LowerGi

__all__ = ["LowerWest3"]


@dataclass
class LowerWest3(
    Gi,
    StrismicGi,
    LowerGi,
    WesternGi,
    ThreeGi,
):
    symbol = "\u2826"
