"""

    *Abstract Letter*

  An abstract letter is an atomic abstract element.

"""

from dataclasses import dataclass

from abc import ABCMeta

__all__ = ["AbstractLetter"]


@dataclass
class AbstractLetter(
    str,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        char: str,
    ):
        assert len(char) == 1, TypeError("Not a character.")
        super(AbstractLetter, self).__new__(
            str,
            char,
        )
