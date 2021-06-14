from dataclasses import dataclass

size = Union[Length, Percentage]


class Dimensions:
    top: Size
    right: Size
    bottom: Size
    left: Size


@dataclass
class Padding:
    block: type
    block_end: type
    block_start: type

    inline: type
    inline_end: type
    inline_start: type
