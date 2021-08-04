"""

    *Yo*   |よ|   |ヨ|

  The _yo_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Yo"]

# [TODO] mechanism of extending


@dataclass
class Yo(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3088"
    katakana = "\u30e8"
