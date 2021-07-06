from enum import Enum

__all__ = ["Visibility"]


class Visiblity(
    Enum,
    Property,
):
    Visible = "visible"  # initial
    Hidden = "hidden"
    Collapse = "collapse"
