"""

    *Opacity-Spectral*

  The spectral measure for opacity.

"""


from wich.measure.scaling import Percent
from wich.measure.spectral import Spectral

__all__ = [
    "OpacitySpectral",
]


class OpacitySpectral(
    Percent,
    Spectral[0, 1],
):
    def __init__(
        self,
        value: float,
    ):
        super(OpacitySpectral, self).__init__(
            value,
        )
