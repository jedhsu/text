"""

Background properties.

"""

from dataclasses import dataclass

from ..base import Image, Property


@dataclass
class Background:
    color: Property
    image: Image

    repeat: Property  # ["no-repeat", "repeat-x", "repeat-y", "repeat"]

    size: Property[Size]

    blend_mode: type
