"""

    *Upper-East 5*   |⠻|

  The upper-east five gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import FiveGi
from .._gi import UpperGi

__all__ = ["UpperEast5"]


@dataclass
class UpperEast5(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    FiveGi,
):
    symbol = "\u283b"
