"""

    *Ge*   |げ|   |ゲ|

  The _ge_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ge"]

# [TODO] mechanism of extending


@dataclass
class Ge(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3052"
    katakana = "\u30b2"
