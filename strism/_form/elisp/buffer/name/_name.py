"""

    *Buffer-Name-Ident*

  The identifier for a buffer name.

"""

from dataclasses import dataclass

from wich._ident import NameIdent

__all__ = [
    "BufferNameIdent",
]


@dataclass
class BufferName:
    name: str
    filename: str
