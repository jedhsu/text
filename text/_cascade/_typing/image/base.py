"""

Image base type.

"""

from dataclasses import dataclass
from typing import Callable


class _Image(type):
    pass


@dataclass
class Paint:
    paint_: Callable

    paint_order: property
