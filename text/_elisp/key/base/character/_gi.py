"""

    *Gi*

  An ordinary character key.

"""

from abc import ABCMeta

from dataclasses import dataclass

from .._key import BaseKey

__all__ = ["Gi"]


@dataclass
class Gi(
    BaseKey,
):
    __metaclass__ = ABCMeta
