"""

    *Level*

  A level on a spectrum between black and white.

"""

from dataclasses import dataclass

from typing import ClassVar

__all__ = ["Level"]


@dataclass
class Level(
    float,
):
    black: ClassVar[float] = -1.0
    white: ClassVar[float] = 1.0

    def __init__(
        self,
        value: float,
    ):
        assert self.black <= value <= self.white, ValueError
        super(Level, self).__new__(
            float,
            value,
        )

    @classmethod
    def create(
        cls,
        value: float,
    ):
        return cls(
            value,
        )
