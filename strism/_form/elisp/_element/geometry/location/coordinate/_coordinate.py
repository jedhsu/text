"""

    Coordinate

  The coordinate type specifies a locational integer.

"""

from wich.literal.integer import Integer

__all__ = [
    "Coordinate",
]


class Coordinate(
    Integer,
):
    def __init__(
        self,
        integer: int,
    ):
        super(Coordinate, self).__init__(
            integer,
        )
