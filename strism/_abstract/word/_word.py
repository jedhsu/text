"""

    *Abstract Word*

  An abstract word is an abstract string whose elements
  are restricted to an abstract letter space.

"""

from dataclasses import dataclass
from strism._abstract.letter import AbstractLetterSpace

from ..string import AbstractString

__all__ = ["AbstractWord"]


@dataclass
class AbstractWord(
    AbstractString,
):
    space: AbstractLetterSpace

    def __init__(
        self,
        string: AbstractString,
        space: AbstractLetterSpace,
    ):
        self.space = space
        super(AbstractWord, self).__init__(
            string,
        )
