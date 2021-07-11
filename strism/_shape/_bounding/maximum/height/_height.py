"""

    *Element Maximum-Height*

  A maximum bound on element height.

"""

from .._maximum import ElementMaximumDimension

__all__ = ["ElementMaximumHeight"]


class ElementMaximumHeight(
    ElementHeightDimension,
    ElementMaximumDimension,
):
    pass
