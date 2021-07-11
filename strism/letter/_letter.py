"""

    *letter*

  A letter is an abstract letter with geometry.

"""

from dataclasses import dataclass

from strism._abstract import AbstractLetter

from ._geometry import LetterGeometry

__all__ = ["Letter"]


@dataclass
class Letter(
    AbstractLetter,
):
    geometry: LetterGeometry
