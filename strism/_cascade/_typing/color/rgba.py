"""

RGB + alpha channel

"""


from typing import Annotated
from dataclasses import dataclass

from ..numeric import Percent


@dataclass
class Rgba(
    Type,
):
    red: Annotated[int, ValueRange(0, 255)]
    green: Annotated[int, ValueRange(0, 255)]
    blue: Annotated[int, ValueRange(0, 255)]
    alpha: Annotated[int, ValueRange(0, 255)]

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
