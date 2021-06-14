"""

Offset property.

"""

from dataclasses import dataclass


@dataclass
class Offset:
    offset: ShorthandProperty

    position: Property
    anchor: Property
    distance: Property
    path: Property
    rotate: Property
