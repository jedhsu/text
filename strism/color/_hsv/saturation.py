"""

    *Saturation*

  The saturation percentage spectral.

"""

from strism._measure.spectral import Spectral

__all__ = ["Saturation"]


class Saturation(
    Spectral[0, 1],
):
    pass
