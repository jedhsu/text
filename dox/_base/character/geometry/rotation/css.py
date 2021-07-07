from dox._form.css import CssProperty

__all__ = ["CssTextOrientation"]


class CssTextOrientation(
    CssProperty,
):
    values = [
        "mixed",
        "upright",
        "sideways",
    ]
