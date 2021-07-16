"""

    *Lower-West 1*   |⠄|

  The lower-west one gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import OneGi
from .._gi import LowerGi

__all__ = ["LowerWest1"]


@dataclass
class LowerWest1(
    Gi,
    StrismicGi,
    LowerGi,
    WesternGi,
    OneGi,
):
    symbol = "\u2804"
