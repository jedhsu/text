"""

    Green Spectral

  The spectral measure for green.

"""

from wich.measure.spectral import Spectral
from wich.literal.integer import Integer

__all__ = [
    "GreenSpectral",
]


class GreenSpectral(
    Integer,
    Spectral,
):
    def __init__(
        self,
        spectral: int,
    ):
        super(GreenSpectral, self).__init__(
            spectral,
        )
