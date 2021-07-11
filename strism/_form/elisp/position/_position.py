"""

    *Position*

  The inder of a character in the text.

  More precisely, a position identifies the place between two characters.

"""


__all__ = ["Position"]


class Position(
    int,
):
    def __init__(
        self,
        position: int,
    ):
        super(BufferPosition, self).__new__(
            int,
            position,
        )
