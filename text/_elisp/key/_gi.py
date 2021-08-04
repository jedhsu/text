"""

    *Gi*

  An atomic key.

  From the japanese *kagi*, 

"""

from dataclasses import dataclass

from typing import Optional


from .base import BaseKey
from .modifier import ModifierKey

__all__ = ["Gi"]


@dataclass
class Gi:
    base: BaseKey
    modifier: Optional[ModifierKey]

    @classmethod
    def create(
        cls,
        base: BaseKey,
        modifier: Optional[ModifierKey] = None,
    ):
        return cls(
            base,
            modifier,
        )
