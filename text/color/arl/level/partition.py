"""

    *Level Partition*

  An n-partition of a level spectrum.

"""

from ._color import Level

from typing import Sequence

__all__ = ["LevelPartition"]


class LevelPartition(
    tuple[Level],
):
    def __init__(
        self,
        levels: Sequence[Level],
    ):
        super(LevelPartition, self).__new__(
            tuple,
            levels,
        )

    def from_spectrum(self):
        """
        Splits evenly from a spectrum.

        """
        pass
