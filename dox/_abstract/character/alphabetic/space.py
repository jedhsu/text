"""

    *Abstract Alphabetic-Space*

"""

from .._character import AbstractCharacter
from ..space import AbstractCharacterSpace

from ._alphabetic import Alphabetic

__all__ = ["AbstractAlphabeticSpace"]

name = "Alphabet"


class AbstractAlphabeticSpace(
    AbstractCharacterSpace,
    Alphabetic,
):
    def __init__(self):
        super(AbstractAlphabeticSpace, self).__init__(
            name,
            {AbstractCharacter(el) for el in space},
        )


space = {
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
}
