"""

    *Cascade: Font-Width*

  The _font-width_ syntax form of the CSS language.

"""

from enum import Enum

from strism._form.cascade import CascadeProperty

__all__ = ["CascadeFontWidth"]

class CascadeFontWidth(
    Enum,
    CascadeProperty,
):
    Light = "Light"
    Normal = "Normal"
    Bold = "Bold"

    # relative
    Lighter = "Lighter"
    Bolder = "Bolder"

    _100 = "100"
    _200 = "200"
    _300 = "300"
    _400 = "400"
    _500 = "500"
    _600 = "600"
    _700 = "700"
    _800 = "800"
    _900 = "900"


# [TODO] think about optimal init design
