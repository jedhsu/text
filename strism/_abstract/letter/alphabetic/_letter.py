"""

    *Abstract Alphabetic-Letter*

"""

from .._letter import AbstractLetter
from ._alphabetic import Alphabetic

__all__ = ["AbstractAlphabeticLetter"]


class AbstractAlphabeticLetter(
    AbstractLetter,
    Alphabetic,
):
    def __init__(
        self,
        char: str,
    ):
        super(AbstractAlphabeticLetter, self).__init__(
            char,
        )
