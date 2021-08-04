"""

    *_U*   |う|   |ウ|

  The _u_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["U"]

# [TODO] mechanism of extending


@dataclass
class U(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3046"
    katakana = "\u30a6"
