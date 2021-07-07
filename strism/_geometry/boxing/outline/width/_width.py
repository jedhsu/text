"""

    *Outline-Width*

"""

from enum import Enum

# [TODO] float is a placeholder, replace with measure


class OutlineWidth(
    Enum,
    float,
):
    Thin = "Thin"
    Medium = "Medium"
    Thick = "Thick"
