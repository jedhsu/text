"""

    *Upper-West 3*   |⠋|

  The upper-west three gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import ThreeGi
from .._gi import UpperGi

__all__ = ["UpperWest3"]


@dataclass
class UpperWest3(
    Gi,
    StrismicGi,
    UpperGi,
    WesternGi,
    ThreeGi,
):
    symbol = "\u280b"
