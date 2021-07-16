"""

    *Upper-West Block*   ⠨

  The upper-west block gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import BlockGi
from .._gi import UpperGi

__all__ = ["UpperWestBlock"]


@dataclass
class UpperWestBlock(
    Gi,
    StrismicGi,
    UpperGi,
    WesternGi,
    BlockGi,
):
    pass
