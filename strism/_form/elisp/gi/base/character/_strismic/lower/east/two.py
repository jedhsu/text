"""

    *Lower-East 2*   |⠰|

  The lower-east two gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import TwoGi
from .._gi import LowerGi

__all__ = ["LowerEast2"]


@dataclass
class LowerEast2(
    Gi,
    StrismicGi,
    LowerGi,
    EasternGi,
    TwoGi,
):
    symbol = "\u2830"
