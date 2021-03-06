"""

    *Pi*   |ぴ|   |ピ|

  The _pi_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Pi"]

# [TODO] mechanism of extending


@dataclass
class Pi(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3074"
    katakana = "\u30d4"
