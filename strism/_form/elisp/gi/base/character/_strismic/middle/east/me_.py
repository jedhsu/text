"""

    *Me2*   ⠨

  The middle-east two gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ...east import EasternGi
from ..._number import TwoGi
from .._gi import MiddleGi

__all__ = ["Me2"]


@dataclass
class Me2(
    Gi,
    MiddleGi,
    EasternGi,
    TwoGi,
):
    symbol = "\u2828"
