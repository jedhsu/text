"""

    X Coordinate

  The x-coordinate.

"""

from ._coordinate import Coordinate

__all__ = [
    "Coordinate",
]


class XCoordinate(
    Coordinate,
):
    def __init__(
        self,
        integer: int,
    ):
        super(XCoordinate, self).__init__(
            integer,
        )
