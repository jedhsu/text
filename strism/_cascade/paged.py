"""

Is this a module?

"""

from dataclasses import dataclass
from typing import Callable


@dataclass
class Page(AtRule):
    size: Callable[[], int]
    marks: Callable
    bleed: Callable


# @right-bottom
# @top-center
# @bottom-center
# etc
