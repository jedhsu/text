"""

    Screen Line

  A screen line is defined by the way text appares on screen.

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
