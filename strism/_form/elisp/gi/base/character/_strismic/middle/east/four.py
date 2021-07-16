"""

    *Middle-East 4*   |⠺|

  The middle-east four gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ...east import EasternGi
from ..._number import FourGi
from .._gi import MiddleGi

__all__ = ["MiddleEast4"]


@dataclass
class MiddleEast4(
    Gi,
    MiddleGi,
    EasternGi,
    FourGi,
):
    symbol = "\u283a"
