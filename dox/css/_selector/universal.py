"""

    *Universal-Selector*

"""


from ._selector import Selector


__all__ = ["UniversalSelector"]


class UniversalSelector(
    Selector,
):
    def __init__(
        self,
        ident: str,
    ):
        super(UniversalSelector, self).__init__(
            ident,
        )
