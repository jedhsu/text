"""

    Marker

  A position in a buffer.

"""

from dataclasses import dataclass

from ..buffer.ident import BufferNameIdent
from ..buffer._position import BufferPosition

__all__ = [
    "Marker",
]


class MarkerInsertionType:
    pass


@dataclass
class Marker:
    buffer: BufferNameIdent
    position: BufferPosition
    insertion_type: MarkerInsertionType
