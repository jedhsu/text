"""

    *Lower-West Block*   ⠨

  The lower-west block gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import BlockGi
from .._gi import LowerGi

__all__ = ["LowerWestBlock"]


@dataclass
class LowerWestBlock(
    Gi,
    StrismicGi,
    LowerGi,
    WesternGi,
    BlockGi,
):
    pass
