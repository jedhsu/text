"""

    *Attribute-Select*

"""

from abc import ABCMeta

from .._select import Select

__all__ = ["AttributeSelect"]


class AttributeSelect(
    Select,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        ident: str,
    ):
        super(AttributeSelect, self).__init__(
            ident,
        )
