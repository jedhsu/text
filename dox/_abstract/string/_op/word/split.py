"""

    *Word-Split*

  Split a string into words based on a character space.

"""

from dataclasses import dataclass

from dox._base.character import CharacterSpace
from dox._base.string import String

from .._operator import StringOperator


@dataclass
class WordSplit(
    StringOperator,
):
    string: String
    space: CharacterSpace
