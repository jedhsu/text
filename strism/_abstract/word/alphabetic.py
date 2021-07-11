"""

    *Abstract Alphabetic-Word*

  An abstract alphabetic-word is an abstract string whose elements
  are restricted to the alphabetic character space.

"""

from strism._abstract.letter import AbstractAlphabeticSpace

from ..string import AbstractString
from ._word import AbstractWord


__all__ = ["AbstractWord"]


class AbstractAlphabeticWord(
    AbstractWord,
):
    def __init__(
        self,
        string: AbstractString,
    ):
        super(AbstractAlphabeticWord, self).__init__(
            string,
            AbstractAlphabeticSpace(),
        )

    @classmethod
    def from_str(
        cls,
        string: str,
    ):
        return cls(
            AbstractString.create(
                string,
            )
        )
