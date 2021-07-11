"""

    *Abstract String*

  An abstract string is a sequence of abstract letters.

  We can partition an abstract string
  based on its abstract word.

"""

from typing import Sequence

from ..letter import AbstractLetter

__all__ = ["AbstractString"]


class AbstractString(
    tuple[AbstractLetter],
):
    def __init__(
        self,
        chars: Sequence[AbstractLetter],
    ):
        super(AbstractString, self).__new__(
            tuple,
            chars,
        )

    @classmethod
    def create(
        cls,
        *char: str,
    ):
        chars = [*char]
        return cls([AbstractLetter(char) for char in chars])

    @classmethod
    def from_str(
        cls,
        string: str,
    ):
        return cls([AbstractLetter(char) for char in string])
