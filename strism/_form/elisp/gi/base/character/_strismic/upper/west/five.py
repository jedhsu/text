"""

    *Upper-West 5*   |⠟|

  The upper-west five gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import FiveGi
from .._gi import UpperGi

__all__ = ["UpperWest5"]


@dataclass
class UpperWest5(
    Gi,
    StrismicGi,
    UpperGi,
    WesternGi,
    FiveGi,
):
    symbol = "\u281f"
