"""

    *Upper-East 1*   |⠈|

  The upper-east one gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import OneGi
from .._gi import UpperGi

__all__ = ["UpperEast1"]


@dataclass
class UpperEast1(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    OneGi,
):
    symbol = "\u2808"
