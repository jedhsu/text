from dataclasses import dataclass
from typing import Callable

from .._type import Type

# class ColorKeyword:
#     pass


class Color(
    Type,
):
    red: Union[int, Percent]
    green: Union[int, Percent]
    blue: Union[int, Percent]

    alpha: Union[int, Percent]

    @classmethod
    def from_keyword(cls):
        pass

    @classmethod
    def from_rgb(cls):
        pass

    @classmethod
    def from_hsl(cls):
        pass

    @classmethod
    def from_lch(cls):
        pass

    @classmethod
    def from_lab(cls):
        """
        From lab coordinate system.

        """
        pass
