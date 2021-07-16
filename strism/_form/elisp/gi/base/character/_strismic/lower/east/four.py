"""

    *Lower-East 4*   |⠼|

  The lower-east four gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import FourGi
from .._gi import LowerGi

__all__ = ["LowerEast4"]


@dataclass
class LowerEast4(
    Gi,
    StrismicGi,
    LowerGi,
    EasternGi,
    FourGi,
):
    symbol = "\u283c"
