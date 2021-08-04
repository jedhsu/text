"""

    *Word*

  A word is an abstract word imbued with geometry.

"""

from dataclasses import dataclass

from dox._abstract.word import AbstractWord


@dataclass
class Word(
    AbstractWord,
):
    geometry: WordGeometry
