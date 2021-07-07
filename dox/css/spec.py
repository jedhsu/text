from dataclasses import dataclass

from typing import Sequence

class Character(
    str,
):
    pass


class Word(
    tuple[Character],
):
    pass


@dataclass
class Chunk:
    description: tuple[Character]


@dataclass
class Line:
    index: int
    characters: Sequence[Character]
    lining: Lining  # describes spacing within a line.

    shading: Shading

class Context:

@dataclass
class Shape:
    index: int
    lines: Sequence[Line]
    geometry: 

@dataclass
class Section:
    name: str
    shapes: Sequence[Shape]
    sectioning: Sectioning  # describes spacing within a section.

