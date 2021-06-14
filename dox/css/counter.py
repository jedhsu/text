"""

Counter. Pseudo class?

"""

from dataclasses import dataclass
from typing import Callable

from ..base import AtRule

counter_: Callable
counters_: Callable

# additive-symbols (@counter-style)


class CounterType(int):
    pass


@dataclass
class Counter:
    counter: type

    increment: property
    reset: property
    set: property
    style_query: property
    counters_call: property


class CounterStyle(AtRule):
    prefix: property
    fallback: property
    negative: property
    pad: property
    range: property
    speak_as: property
    suffix: property
    system: property
    symbols: property
