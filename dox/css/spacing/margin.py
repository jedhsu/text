from dataclasses import dataclass


class MarginDimensions(Dimensions):
    bottom: type
    left: type
    right: type
    top: type


@dataclass
class Margin:
    block: type
    block_start: type
    block_end: type

    inline: type
    inline_start: type
    inline_end: type

    trim: type
