"""

    Count

  The counting measure.

"""

from wich.literal.integer import Integer

from ._measure import Measure

__all__ = [
    "Count",
]


class Count(
    Integer,
    Measure,
):
    def __init__(
        self,
        integer: int,
    ):
        super(Count, self).__init__(
            integer,
        )
