"""

    *Ri*   |り|   |リ|

  The _ri_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ri"]

# [TODO] mechanism of extending


@dataclass
class Ri(
    Gi,
    JapaneseGi,
):
    hiragana = "\u308a"
    katakana = "\u30ea"
