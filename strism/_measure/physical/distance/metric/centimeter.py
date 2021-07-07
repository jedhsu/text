"""

    Centimeter

  The metric centimeter unit distance measure.

"""

from abc import ABCMeta

from ..._unit import UnitDistance
from ._distance import MetricDistance

from wich.literal.float_ import Float

__all__ = [
    "Centimeter",
]


class Centimeter(
    Float,
    MetricDistance,
    UnitDistance,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        float: float,
    ):
        super(Centimeter, self).__init__(
            float,
        )
