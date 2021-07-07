"""

    *Word-Split*

  Split a string into words based on a character space.

"""

from dataclasses import dataclass

from strism._abstract.character import AbstractCharacterSpace
from strism._abstract.string import AbstractString

from .._operator import StringOperator

__all__ = ["WordSplit"]


@dataclass
class WordSplit(
    StringOperator,
):
    string: AbstractString
    space: AbstractCharacterSpace
