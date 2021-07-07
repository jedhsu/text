"""

    *Attribute-Partial-Value-Select*

  Select based on attribute value.

"""

from abc import ABCMeta

from ._select import AttributeValueSelect

__all__ = ["AttributePartialValueSelect"]


class AttributePartialValueSelect(
    AttributeValueSelect,
):
    __metaclass__ = ABCMeta
