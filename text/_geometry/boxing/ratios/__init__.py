"""

    box ratios

"""

from ._ratio import BoxRatio

from .padding import PaddingBoxRatio
from .border import BorderBoxRatio
from .margin import MarginBoxRatio

from ._ratios import BoxRatios

__all__ = [
    "BoxRatio",
    "PaddingBoxRatio",
    "BorderBoxRatio",
    "MarginBoxRatio",
    "BorderBoxRatio",
]
