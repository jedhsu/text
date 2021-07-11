"""

    Basic Window Parameters

"""

from typing import Literal
from dataclasses import dataclass

__all__ = [
    "BasicWindowParameters",
]


@dataclass
class BasicWindowParameters(
    WindowParameters,
):
    display: Display
    display_color: Literal[
        "color",
        "Grayscale",
        "mono",
    ]
    title: str
    name: str
    explicit_name: str
