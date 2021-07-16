"""

    *North-East Block*   ⠨

  The north-east block gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import BlockGi
from .._gi import NorthernGi

__all__ = ["NorthEastBlock"]


@dataclass
class NorthEastBlock(
    Gi,
    StrismicGi,
    NorthernGi,
    EasternGi,
    BlockGi,
):
    pass
