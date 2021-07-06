"""

    *Universal-Element-Selector*   *

  Universal element selector.

  Implicit when a non-element selector is written.

"""


from ._selector import Selector


__all__ = ["UniversalElementSelector"]


class UniversalElementSelector(
    Selector,
):
    def __init__(
        self,
        ident: str,
    ):
        super(UniversalElementSelector, self).__init__(
            ident,
        )
