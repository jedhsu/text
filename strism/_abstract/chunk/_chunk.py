"""

    *Abstract Chunk*

  An abstract chunk is an abstract word
  that contains an abstract word.

  Traditionally inline.

"""

from dataclasses import dataclass

from ..letter import AbstractLetterSpace
from ..word import AbstractWord


__all__ = ["AbstractChunk"]


@dataclass
class AbstractChunk(
    AbstractWord,
):
    element: AbstractWord

    def __init___(
        self,
        word: AbstractWord,
        element: AbstractWord,
        space: AbstractLetterSpace,
    ):
        self.element = element
        super(AbstractChunk, self).__init__(
            word,
            space,
        )
