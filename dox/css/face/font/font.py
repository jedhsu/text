from dataclasses import dataclass
from enum import Enum
from typing import Annotated, Callable

from dox.css._base import Property

from . import AtRule


@dataclass
class Font:

    font_size: property
    font_size_adjust: property

    font_stretch: property
    font_style: property

    font_variation_settings: property
    font_weight: property


class FontSynthesis(Property):
    pass


@dataclass
class Local:
    """
    Install font locally.

    """

    local_: Callable