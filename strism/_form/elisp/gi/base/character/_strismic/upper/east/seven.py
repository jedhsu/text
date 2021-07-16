"""

    *Upper-East 7*

  The upper-east seven gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import SevenGi
from .._gi import UpperGi

__all__ = ["UpperEast7"]


@dataclass
class UpperEast7(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    SevenGi,
):
    symbol = "\u2828"
