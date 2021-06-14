"""

Background properties.

"""

from dataclasses import dataclass


@dataclass
class Background:
    color: Property
    image: Property

    repeat: Property  # ["no-repeat", "repeat-x", "repeat-y", "repeat"]

    size: Property[Size]

    position: type

    attachment: type
    blend_mode: type
    clip: type
    origin: type
