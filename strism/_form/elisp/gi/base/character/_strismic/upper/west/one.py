"""

    *Upper-West 1*   ⠨

  The upper-west one gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import OneGi
from .._gi import UpperGi

__all__ = ["UpperWest1"]


@dataclass
class UpperWest1(
    Gi,
    StrismicGi,
    UpperGi,
    WesternGi,
    OneGi,
):
    symbol = "\u2828"
