from typing import Annotated
from dataclasses import dataclass

from ..numeric import Percent


@dataclass
class Hsla(
    Type,
):
    hue: Annotated[int, ValueRange(0, 360)]
    saturation: Percent
    light: Percent
    alpha: Percent

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
