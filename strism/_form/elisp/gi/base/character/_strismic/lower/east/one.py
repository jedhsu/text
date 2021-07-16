"""

    *Lower-East 1*   |⠠|

  The lower-east one gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import OneGi
from .._gi import LowerGi

__all__ = ["LowerEast1"]


@dataclass
class LowerEast1(
    Gi,
    StrismicGi,
    LowerGi,
    EasternGi,
    OneGi,
):
    symbol = "\u2820"
