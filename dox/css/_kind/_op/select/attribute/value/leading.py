"""

    *Attribute-Leading-Value-Select*

  Select based on attribute value.

"""

from abc import ABCMeta

from ._select import AttributeValueSelect

__all__ = ["AttributeLeadingValueSelect"]


class AttributeLeadingValueSelect(
    AttributeValueSelect,
):
    __metaclass__ = ABCMeta
