"""

    *Ro*   |ろ|   |ロ|

  The _ro_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Ro"]

# [TODO] mechanism of extending


@dataclass
class Ro(
    Gi,
    JapaneseGi,
):
    hiragana = "\u308d"
    katakana = "\u30ed"
