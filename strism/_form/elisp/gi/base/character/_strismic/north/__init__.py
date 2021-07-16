"""

    *key . atom . base . char . pos . nor*

  North hemisphere positional character keys.

"""

from ._gi import NorthernGi

from .west import NorthWest1
from .west import NorthWest2
from .west import NorthWest3
from .west import NorthWest4
from .west import NorthWest5
from .west import NorthWest6
from .west import NorthWest7

from .east import NorthEast1
from .east import NorthEast2
from .east import NorthEast3
from .east import NorthEast4
from .east import NorthEast5
from .east import NorthEast6
from .east import NorthEastBlock

__all__ = [
    "NorthernGi",
    "NorthWest1",
    "NorthWest2",
    "NorthWest3",
    "NorthWest4",
    "NorthWest5",
    "NorthWest6",
    "NorthWest7",
    "NorthEast1",
    "NorthEast2",
    "NorthEast3",
    "NorthEast4",
    "NorthEast5",
    "NorthEast6",
    "NorthEastBlock",
]
