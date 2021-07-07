"""

    *Abstract Line*

  A line is a sequence of abstract words.

"""

from typing import Sequence

from ..word import AbstractWord


class AbstractLine(
    tuple[AbstractWord],
):
    def __init__(
        self,
        words: Sequence[AbstractWord],
    ):
        super(AbstractLine, self).__new__(
            tuple,
            words,
        )
