"""

    *Dji*   |ぢ|   |ヂ|

  The _dji_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Dji"]

# [TODO] mechanism of extending


@dataclass
class Dji(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3062"
    katakana = "\u30c2"
