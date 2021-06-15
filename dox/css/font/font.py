from dataclasses import dataclass
from enum import Enum
from typing import Annotated, Callable

from . import AtRule


@dataclass
class FontFace(AtRule):
    line_gap_override: Annotated[
        bool, property
    ]  # [TODO] keep playing with this - but we want to clarify it's return. Time for Annotated

    range: property
    src: property
    size_adjust: property
    ascent_override: property


class FontFace(AtRule):
    @property
    def descent_override(self) -> Union[Normal, Percentage]:
        pass


class FontStretch:
    Normal = "normal"

    UltraCondensed = "ultra-condensed"
    ExtraCondensed = "extra-condensed"
    Condensed = "condensed"
    SemiCondensed = "semi-condensed"

    SemiExpanded = "semi-expanded"
    Expanded = "expanded"
    ExtraExpanded = "extra-expanded"
    UltraExpanded = "ultra-expanded"


@dataclass
class Font:
    font: property

    font_face: AtRule

    font_feature_settings: type

    font_kerning: property
    font_language_override: property
    font_optical_sizing: property

    font_size: property
    font_size_adjust: property

    font_stretch: property
    font_style: property
    font_synthesis: property

    font_variation_settings: property
    font_weight: property


@dataclass
class Unicode:
    """
    Font descriptor.

    """

    bidi: property


@dataclass
class Local:
    """
    Install font locally.

    """

    local_: Callable


class FontStyle:
    Normal = "Normal"
    Italic = "Italic"
    Oblique = "Oblique"
    Inherit = "Inherit"


class FontWeightKeyword:
    Light = "Light"
    Normal = "Normal"
    Bold = "Bold"

    # relative
    Lighter = "Lighter"
    Bolder = "Bolder"


# 400 - normal, 700 - bold
FontWeightNumericKeyword = [100, 200, 300, 400, 500, 600, 700, 800, 900]


class FontSize:
    """
    Length value or keyword.

    """

    pass


class FontSizeKeyword:
    """
    Semi-absolute keyword.

    """

    XXSmall = "xx-small"
    XSmall = "x-small"
    Small = "small"
    Medium = "medium"
    Large = "large"
    XLarge = "x-large"
    XXLarge = "xx-large"

    Smaller = "smaller"
    Larger = "larger"


@dataclass
class Variant:
    decorated_font_face: type
    alternates: type
    caps: type
    east_asian: type
    ligatures: type
    numeric: type
    position: type
