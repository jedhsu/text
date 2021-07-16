"""

    *Upper-East 2*   |⠘|

  The upper-east two gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import TwoGi
from .._gi import UpperGi

__all__ = ["UpperEast2"]


@dataclass
class UpperEast2(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    TwoGi,
):
    symbol = "\u2818"
