"""

    *Attribute-Exact-Value-Select*

  Select based on attribute value.

"""

from abc import ABCMeta

from ._select import AttributeValueSelect

__all__ = ["AttributeExactValueSelect"]


class AttributeExactValueSelect(
    AttributeValueSelect,
):
    __metaclass__ = ABCMeta
