"""

    *Middle-East Block*   ⠨

  The middle-east block gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ...east import EasternGi
from ..._number import BlockGi
from .._gi import MiddleGi

__all__ = ["MiddleEastBlock"]


@dataclass
class MiddleEastBlock(
    Gi,
    MiddleGi,
    EasternGi,
    BlockGi,
):
    pass
