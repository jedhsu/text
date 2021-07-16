"""

    *A*   |あ|   |ア|

  The _a_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["A"]

# [TODO] mechanism of extending


@dataclass
class A(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3042"
    katakana = "\u30a2"
