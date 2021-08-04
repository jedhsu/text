"""

    *Da*   |だ|   |ダ|

  The _da_ Japanese gi.

"""

from dataclasses import dataclass

from strism._form.elisp.gi.base.character._strismic import MiddleEast2

from ...._gi import Gi
from ..._gi import JapaneseGi


__all__ = ["Da"]

# [TODO] mechanism of extending


@dataclass
class Da(
    Gi,
    JapaneseGi,
):
    hiragana = "\u3060"
    katakana = "\u30c0"
