"""

    *Lower-West 2*   |⠆|

  The lower-west two gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import TwoGi
from .._gi import LowerGi

__all__ = ["LowerWest2"]


@dataclass
class LowerWest2(
    Gi,
    StrismicGi,
    LowerGi,
    WesternGi,
    TwoGi,
):
    symbol = "\u2806"
