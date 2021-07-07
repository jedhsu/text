"""

    *Abstract Alphabetic-Character*

"""

from .._character import AbstractCharacter
from ._alphabetic import Alphabetic

__all__ = ["AbstractAlphabeticCharacter"]


class AbstractAlphabeticCharacter(
    AbstractCharacter,
    Alphabetic,
):
    def __init__(
        self,
        char: str,
    ):
        super(AbstractAlphabeticCharacter, self).__init__(
            char,
        )
