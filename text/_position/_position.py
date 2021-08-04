"""

    *Element Position*

"""

from dataclasses import dataclass

from .xpos import ElementXpos
from .ypos import ElementYpos

__all__ = ["ElementPosition"]

# [TODO] integrate measure


@dataclass
class ElementPosition:
    x: ElementXpos
    y: ElementYpos

    @classmethod
    def create(
        cls,
        x: int,
        y: int,
    ):
        return cls(
            ElementXpos(x),
            ElementYpos(y),
        )
