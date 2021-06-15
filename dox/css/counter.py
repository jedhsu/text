"""

Counter. Pseudo class?

"""

from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

from ..base import AtRule
from .base import CustomIdent

counter_: Callable
counters_: Callable

# additive-symbols (@counter-style)


class CounterType(int):
    pass


T = TypeVar("T", CustomIdent, int, None)


class CounterIncrement(Generic[T]):
    pass


class CounterReset(Generic[T]):
    pass


@dataclass
class Counter:
    counter: type

    increment: CounterIncrement

    reset: CounterReset

    set: property
    style_query: property

    # [TODO] what are these args
    counters_call: property


class CounterStyle(AtRule):
    prefix: property
    fallback: property
    negative: property
    pad: property
    range: property
    speak_as: property
    suffix: property
    # [TODO] how implement descriptors?
    system: Descriptor
    symbols: property
