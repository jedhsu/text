"""

    *Abstract String*

  An abstract string is a sequence of abstract characters.

  We can partition an abstract string
  based on its abstract word.

"""

from typing import Sequence

from ..character import AbstractCharacter

__all__ = ["AbstractString"]


class AbstractString(
    tuple[AbstractCharacter],
):
    def __init__(
        self,
        chars: Sequence[AbstractCharacter],
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
        return cls([AbstractCharacter(char) for char in chars])

    @classmethod
    def from_str(
        cls,
        string: str,
    ):
        return cls([AbstractCharacter(char) for char in string])
