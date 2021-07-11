"""

    *Line*

  A line is a string within the buffer text.

"""

from typing import Sequence
from abc import ABCMeta
from dataclasses import dataclass

from wich.literal.character import Character


__all__ = [
    "Line",
]


@dataclass
class Line(
    String,
):
    __metaclass__ = ABCMeta

    index: int

    def __init__(
        self,
        index: int,
        string: String,
    ):
        self.index = index
        super(Line, self).__init__(
            String,
        )
