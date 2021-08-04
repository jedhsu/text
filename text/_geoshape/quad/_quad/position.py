"""

    *Quad Position*

  The position of a quad.

"""

from dataclasses import dataclass

from strism._position import ElementPosition
from strism._position import ElementXpos
from strism._position import ElementYpos

__all__ = ["QuadPosition"]


@dataclass
class QuadPosition(
    ElementPosition,
):
    def __init__(
        self,
        xpos: ElementXpos,
        ypos: ElementYpos,
    ):
        super(QuadPosition, self).__init__(
            xpos,
            ypos,
        )
