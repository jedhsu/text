"""

    *Context*

  A context is a container with an additional attribute of its container type.

"""


from dataclasses import dataclass

from abc import ABCMeta

from typing import TypeVar
from typing import Generic

from .._container import Container


T = TypeVar("T")


@dataclass
class Context(
    Generic[T],
    Container[T],
):
    __metaclass__ = ABCMeta

    context: Container[T]
