"""

    *Green*

  The spectral measure for green.

"""

__all__ = ["Green"]

from ._primary import PrimaryColor


class Green(
    PrimaryColor,
):
    def __init__(
        self,
        val: int,
    ):
        super(Green, self).__init__(
            val,
        )
