"""

    *Point*

  The buffer position where editing takes place.

  A frequent operator is to *move* the point.

"""

from wich.editor.position import Position

__all__ = ["Cursor"]


class Cursor(
    Position,
):
    def __init__(
        self,
        val: int,
    ):
        super(Cursor, self).__init__(val)
