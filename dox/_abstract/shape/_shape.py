"""

    *Abstract Shape*

  An abstract shape is a sequence of abstract lines.

"""

from typing import Sequence

from ..word import AbstractWord

__all__ = ["AbstractShape"]


class AbstractShape(
    tuple[AbstractWord],
):
    def __init__(
        self,
        words: Sequence[AbstractWord],
    ):
        super(AbstractShape, self).__new__(
            tuple,
            words,
        )
