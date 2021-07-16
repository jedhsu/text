"""

    *Tsu*   |む|   |ム|

  The _tsu_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Tsu"]

# [TODO] mechanism of extending


@dataclass
class Tsu(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3064"
    katakana = "\u30c4"
