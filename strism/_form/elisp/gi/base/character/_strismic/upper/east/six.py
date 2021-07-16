"""

    *Upper-East 6*

  The upper-east six gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import SixGi
from .._gi import UpperGi

__all__ = ["UpperEast6"]


@dataclass
class UpperEast6(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    SixGi,
):
    symbol = "\u2828"
