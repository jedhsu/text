"""

    *Abstract Alphabetic-Space*

"""

from .._letter import AbstractLetter
from ..space import AbstractLetterSpace

from ._alphabetic import Alphabetic

__all__ = ["AbstractAlphabeticSpace"]

name = "Alphabet"


class AbstractAlphabeticSpace(
    AbstractLetterSpace,
    Alphabetic,
):
    def __init__(self):
        super(AbstractAlphabeticSpace, self).__init__(
            name,
            {AbstractLetter(el) for el in space},
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
