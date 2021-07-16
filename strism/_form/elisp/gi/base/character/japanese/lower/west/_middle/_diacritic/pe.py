"""

    *Pe*   |ぺ|   |ペ|

  The _pe_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Pe"]

# [TODO] mechanism of extending


@dataclass
class Pe(
    Gi,
    JapaneseGi,
):
    hiragana = "\u307a"
    katakana = "\u30da"
