"""

    *Geometry*

  An element is defined by its geometry, which removes it from the abstract.

"""

__all__ = ["Geometry"]


class Geometry(
    Shaping,
    Positioning,
    Coloring,
    Boxing,
):
    pass
