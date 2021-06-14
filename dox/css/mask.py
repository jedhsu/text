from dataclasses import dataclass


@dataclass
class MaskBorder:
    border: type
    mode: type
    outset: type
    repeat: type
    slice: type
    source: type
    width: type


@dataclass
class Mask:
    mode: type

    mask: type
    border: MaskBorder
    clip: type
    composite: type
    image: type
    origin: type
    position: type
    repeat: type
    size: type
    type: type
