"""

    *Border-Width*

"""

from enum import Enum

# [TODO] float is a placeholder, replace with measure


class BorderWidth(
    Enum,
    float,
):
    Thin = "Thin"
    Medium = "Medium"
    Thick = "Thick"
