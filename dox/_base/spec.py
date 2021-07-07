from dataclasses import dataclass


class Word(
    tuple[Character],
):
    pass


@dataclass
class Chunk(
    tuple[Character],
):
    pass


@dataclass
class Shape(
    tuple[Character],
):
    pass
