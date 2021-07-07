"""

    *Gradient*

"""

from abc import ABCMeta

from dataclasses import dataclass
from typing import Callable

from .base import Image


@dataclass
class Gradient(Image):
    __metaclass__ = ABCMeta

    conic_gradient: Callable
    linear_gradient_: Callable
    radial_gradient_: Callable

    # repeating_linear_gradient_: Callable
    # repeating_radial_gradient_: Callable


class RepeatingGradient(Gradient):
    linear: Callable
    radial: Callable
