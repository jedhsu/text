from dataclasses import dataclass

from ..base import Property
from ..measure import Length, Percentage


class Keyword:
    MaxContent = "max-content"
    MinContent = "min-content"
    # [TODO] fit-content
    Auto = "auto"


@dataclass
class Width(
    Length,
    Percentage,
    Keyword,
    GlobalKeyword,
    Property,
):
    max_width: Property
    min_width: Property


@dataclass
class Height(Property):
    max_height: Property
    min_height: Property


@dataclass
class Dimensions:
    width: Width
    height: Height


@dataclass
class Clip:
    """
    Visible portion.

    """

    # [TODO] move to animation?

    clip: property
    clip_path: property
