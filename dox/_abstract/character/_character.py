"""

    *Abstract Character*

  An abstract character is an atomic abstract element.

"""

from dataclasses import dataclass

from abc import ABCMeta

__all__ = ["AbstractCharacter"]


@dataclass
class AbstractCharacter(
    str,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        char: str,
    ):
        super(AbstractCharacter, self).__new__(
            str,
            char,
        )
