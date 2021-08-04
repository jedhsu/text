"""

    *Tone*

  A color with an accent, indexed by a level.

"""

from dataclasses import dataclass

from .._color import Color

__all__ = ["Tone"]


@dataclass
class Tone(
    Color,
):
    level: int
    accent: Color
