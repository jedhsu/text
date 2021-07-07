"""

    *Attribute-Value-Select*

  Select based on attribute value.

"""

from abc import ABCMeta

from .._select import AttributeSelect

__all__ = ["AttributeValueSelect"]


class AttributeValueSelect(
    AttributeSelect,
):
    __metaclass__ = ABCMeta
