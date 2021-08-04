"""

    *Abstract Page*

  A page is a dictionary of abstract blocks.

"""

from ..block import AbstractBlock

__all__ = ["AbstractPage"]


class AbstractPage(
    dict[str, AbstractBlock],
):
    pass
