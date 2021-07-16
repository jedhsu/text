"""

    *To*   |と|   |ト|

  The _to_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["To"]

# [TODO] mechanism of extending


@dataclass
class To(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3068"
    katakana = "\u30c8"
