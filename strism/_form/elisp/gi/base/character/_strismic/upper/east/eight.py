"""

    *Upper-East 8*

  The upper-east eight gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import EightGi
from .._gi import UpperGi

__all__ = ["UpperEast8"]


@dataclass
class UpperEast8(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    EightGi,
):
    symbol = "\u2828"
