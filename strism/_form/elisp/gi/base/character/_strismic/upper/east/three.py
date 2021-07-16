"""

    *Upper-East 3*   |⠙|

  The upper-east three gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import ThreeGi
from .._gi import UpperGi

__all__ = ["UpperEast3"]


@dataclass
class UpperEast3(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    ThreeGi,
):
    symbol = "\u2819"
