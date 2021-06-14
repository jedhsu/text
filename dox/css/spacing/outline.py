"""

Similar to border.

"""

from dataclasses import dataclass


@dataclass
class Outline:
    color: type
    offset: type
    outline_style: Property
    outline_width: Property
