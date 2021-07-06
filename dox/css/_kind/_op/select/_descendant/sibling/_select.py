"""

    *Sibling-Select*

  Select based on node siblings.

"""

from .._select import DescendantSelect

__all__ = ["SiblingSelect"]


class SiblingSelect(
    DescendantSelect,
):
    pass
