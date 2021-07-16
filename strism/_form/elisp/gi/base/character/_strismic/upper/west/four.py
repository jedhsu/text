"""

    *Upper-West 4*   |⠏|

  The upper-west four gi.

"""

from dataclasses import dataclass

from ...._gi import Gi
from ..._gi import StrismicGi
from ...west import WesternGi
from ..._number import FourGi
from .._gi import UpperGi

__all__ = ["UpperWest4"]


@dataclass
class UpperWest4(
    Gi,
    StrismicGi,
    UpperGi,
    WesternGi,
    FourGi,
):
    symbol = "\u280f"
