"""

    *String Texturing*

  The texture attributes of string geometry.

"""

from dataclasses import dataclass

from .kerning import StringKerning

__all__ = ["StringTexturing"]


@dataclass
class StringTexturing:
    kerning: StringKerning

    def __init__(
        self,
        kerning: StringKerning,
        *args,
        **kwargs,
    ):
        self.kerning = kerning
        super(StringTexturing, self).__init__(
            *args,
            **kwargs,
        )
