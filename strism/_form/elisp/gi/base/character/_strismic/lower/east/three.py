"""

    *Lower-East 3*   ⠨

  The lower-east three gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import ThreeGi
from .._gi import LowerGi

__all__ = ["LowerEast3"]


@dataclass
class LowerEast3(
    Gi,
    StrismicGi,
    LowerGi,
    EasternGi,
    ThreeGi,
):
    symbol = "\u2828"
