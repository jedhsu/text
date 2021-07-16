"""

    *Du*   |づ|   |ヅ|

  The _du_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Du"]

# [TODO] mechanism of extending


@dataclass
class Du(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3065"
    katakana = "\u30c5"
