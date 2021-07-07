"""

    *Cascade: Hanging-Punctuation*

  Hanging-punctuation, the CSS property syntax form.

  Specifies whether punctuation should hang
  at the start or end of a line of text.

"""

from strism._form.cascade import CascadeProperty

__all__ = ["CascadeHangingPunctuation"]


class CascadeHangingPunctuation(
    CascadeProperty,
):
    None_ = "none"

    First = "first"
    Last = "last"
    ForceEnd = "force-end"
    AllowEnd = "allow-end"
