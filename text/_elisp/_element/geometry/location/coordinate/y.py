"""

    Y Coordinate

  The y-coordinate.

"""

from ._coordinate import Coordinate

__all__ = [
    "Coordinate",
]


class YCoordinate(
    Coordinate,
):
    def __init__(
        self,
        integer: int,
    ):
        super(YCoordinate, self).__init__(
            integer,
        )
