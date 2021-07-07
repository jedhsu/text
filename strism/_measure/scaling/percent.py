"""

    Percent

  The percentage scaling measure.

"""

from wich.literal.float_ import Float


from ._measure import ScalingMeasure

__all__ = [
    "Percent",
]


class Percent(
    Float,
    ScalingMeasure,
):
    def __init__(
        self,
        float: float,
    ):
        assert 0 <= float <= 1, "Percent must be between 0 and 1."
        super(Percent, self).__init__(
            float,
        )
