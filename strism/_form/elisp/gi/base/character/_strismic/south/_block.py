"""

    *South Block*   ⠨

  The south block gi.

"""

from dataclasses import dataclass

from ..._gi import Gi
from .._number import BlockGi
from ._gi import SouthernGi

__all__ = ["SouthBlock"]


@dataclass
class SouthBlock(
    Gi,
    SouthernGi,
    BlockGi,
):
    pass
