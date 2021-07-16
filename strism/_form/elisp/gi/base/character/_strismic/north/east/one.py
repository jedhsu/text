"""

    *North-East 1*   ⠨

  The north-east one gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import OneGi
from .._gi import NorthernGi

__all__ = ["NorthEast1"]


@dataclass
class NorthEast1(
    Gi,
    StrismicGi,
    NorthernGi,
    EasternGi,
    OneGi,
):
    symbol = "\u2828"
