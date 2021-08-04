"""

    *Geometry*

  An element is defined by its geometry, which removes it from the abstract.

"""

from .boxing import Boxing
from .coloring import Coloring
from .positioning import Positioning
from .shaping import Shaping

__all__ = ["Geometry"]


class Geometry(
    Shaping,
    Positioning,
    Coloring,
    Boxing,
):
    pass
