"""

    *Container*

  A container contains elements.

"""

from dataclasses import dataclass

from abc import ABCMeta

from typing import Sequence
from typing import Optional
from typing import TypeVar
from typing import Generic

T = TypeVar("T")


@dataclass
class Container(
    Generic[T],
):
    __metaclass__ = ABCMeta

    index: Optional[int]
    name: Optional[str]
    elements: Sequence[T]

    geometry: Geometry
