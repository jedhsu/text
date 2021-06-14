"""

Transition module.

"""

from dataclasses import dataclass
from typing import Callable


@dataclass
class Transition:
    delay: type
    duration: type
    property: type
    timing_function: type


class TransitionTimingFunction:
    # [TODO] clarify
    steps_: Callable
    cubic_bezier: Callable
