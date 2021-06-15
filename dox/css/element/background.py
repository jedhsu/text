"""

Background properties.

"""

from dataclasses import dataclass

from ..base import Image, Property


class BackgroundOrigin:
    BorderBox = "border-box"
    PaddingBox = "padding-box"
    ContentBox = "content-box"


class BackgroundClip:
    BorderBox = "border-box"
    PaddingBox = "padding-box"
    ContentBox = "content-box"


@dataclass
class Background:
    color: Property
    image: Image

    repeat: Property  # ["no-repeat", "repeat-x", "repeat-y", "repeat"]

    size: Property[Size]

    position: type

    attachment: type
    blend_mode: type

    origin: BackgroundOrigin
    clip: BackgroundClip
