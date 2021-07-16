"""

    *South-East 1*   |⠠|

  The south-east one gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import OneGi
from .._gi import SouthernGi

__all__ = ["SouthEast1"]


@dataclass
class SouthEast1(
    Gi,
    StrismicGi,
    SouthernGi,
    EasternGi,
    OneGi,
):
    symbol = "\u2820"
