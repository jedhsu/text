"""

    *Middle-West Block*   ⠨

  The middle-west block gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ...west import WesternGi
from ..._number import BlockGi
from .._gi import MiddleGi

__all__ = ["MiddleWestBlock"]


@dataclass
class MiddleWestBlock(
    Gi,
    MiddleGi,
    WesternGi,
    BlockGi,
):
    pass
