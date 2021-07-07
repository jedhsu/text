"""

    *Abstract Block*

  An abstract block is a dictionary of abstract shapes.

"""

from ..shape import AbstractShape

__all__ = ["AbstractBlock"]


class AbstractBlock(
    dict[str, AbstractShape],
):
    pass
