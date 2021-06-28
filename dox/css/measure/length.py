from dataclasses import dataclass
from typing import Callable

from .base import AbsoluteMeasure

__all__ = ["Length"]

calc: Callable


class Length(AbsoluteLength, RelativeLength):
    pass
