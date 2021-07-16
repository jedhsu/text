"""

    *Upper-East Block*   ⠨

  The upper-east block gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...east import EasternGi
from ..._number import BlockGi
from .._gi import UpperGi

__all__ = ["UpperEastBlock"]


@dataclass
class UpperEastBlock(
    Gi,
    StrismicGi,
    UpperGi,
    EasternGi,
    BlockGi,
):
    pass
