"""

    *Abstract Word*

  An abstract word is an abstract string whose elements
  are restricted to an abstract character space.

"""

from dataclasses import dataclass
from dox._abstract.character import AbstractCharacterSpace

from ..string import AbstractString

__all__ = ["AbstractWord"]


@dataclass
class AbstractWord(
    AbstractString,
):
    space: AbstractCharacterSpace

    def __init__(
        self,
        string: AbstractString,
        space: AbstractCharacterSpace,
    ):
        self.space = space
        super(AbstractWord, self).__init__(
            string,
        )
