"""

    *Lower-East Block*   ⠨

  The lower-east block gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import BlockGi
from .._gi import LowerGi

__all__ = ["LowerEastBlock"]


@dataclass
class LowerEastBlock(
    Gi,
    StrismicGi,
    LowerGi,
    EasternGi,
    BlockGi,
):
    pass
