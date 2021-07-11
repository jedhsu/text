"""

    *Coordinate*

"""

__all__ = ["Coordinate"]


class Coordinate(
    int,
):
    def __init__(
        self,
        integer: int,
    ):
        super(Coordinate, self).__new__(
            int,
            integer,
        )
