"""

    *Lower-East 5*   |⠾|

  The lower-east five gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import FiveGi
from .._gi import LowerGi

__all__ = ["LowerEast5"]


@dataclass
class LowerEast5(
    Gi,
    StrismicGi,
    LowerGi,
    EasternGi,
    FiveGi,
):
    symbol = "\u283e"
