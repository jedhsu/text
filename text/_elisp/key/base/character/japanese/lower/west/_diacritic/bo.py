"""

    *Bo*   |ぼ|   |ボ|

  The _bo_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Bo"]

# [TODO] mechanism of extending


@dataclass
class Bo(
    Gi,
    JapaneseGi,
):
    hiragana = "\u307c"
    katakana = "\u30dc"
