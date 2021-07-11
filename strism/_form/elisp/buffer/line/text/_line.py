"""

    Text Line

  A text line is defined by delimited newline characters in the buffer text.

"""


from typing import Sequence
from abc import ABCMeta
from dataclasses import dataclass

from wich.literal.character import Character


__all__ = [
    "Line",
]


class ScreenLine(
    Line,
):
    def __init__(
        self,
        index: int,
        string: String,
    ):
        pass
