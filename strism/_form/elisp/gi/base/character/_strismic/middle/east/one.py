"""

    *Middle-East 1*   |⠐|

  The middle-east one gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ...east import EasternGi
from ..._number import OneGi
from .._gi import MiddleGi

__all__ = ["MiddleEast1"]


@dataclass
class MiddleEast1(
    Gi,
    MiddleGi,
    EasternGi,
    OneGi,
):
    symbol = "\u2810"
