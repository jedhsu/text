"""

Text Case Transform

Case transformation operator for text.

"""

__all__ = ["ElementOperator"]


class TextTransform(
    ElementOperator,
):

    # keyword = "text-transform"

    Capitalize = "capitalize"
    Uppercase = "uppercase"
    Lowercase = "lowercase"
    None_ = "none"  # disable
