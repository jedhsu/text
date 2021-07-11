"""

    *Primary Color*

"""

from abc import ABCMeta

__all__ = ["PrimaryColor"]


class PrimaryColor(
    int,
    # Spectral,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        val: int,
    ):
        assert 0 <= val <= 255
        super(PrimaryColor, self).__new__(
            int,
            val,
        )
