"""

    *Upper-East 4*   |⠹|

  The upper-east four gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import FourGi
from .._gi import UpperGi

__all__ = ["UpperEast4"]


@dataclass
class UpperEast4(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    FourGi,
):
    symbol = "\u2839"
