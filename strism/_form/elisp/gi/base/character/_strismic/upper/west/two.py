"""

    *Upper-West 2*   |⠃|

  The upper-west two gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import TwoGi
from .._gi import UpperGi

__all__ = ["UpperWest2"]


@dataclass
class UpperWest2(
    Gi,
    StrismicGi,
    UpperGi,
    WesternGi,
    TwoGi,
):
    symbol = "\u2803"
